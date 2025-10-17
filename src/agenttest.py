from cgitb import reset 
import json
import time
import pandas as pd
from tqdm import tqdm
import os
import asyncio
import glob
import openai
import inspect
from datetime import datetime
import re
from pathlib import Path

from typing import Any, Dict, Callable, List
from .config import ModelRegistry
from mcp import ClientSession, StdioServerParameters
from autogen_ext.tools.mcp import StdioServerParams, mcp_server_tools

from autogen_agentchat.agents import AssistantAgent
from autogen_agentchat.messages import TextMessage
from autogen_core import CancellationToken
from autogen_ext.models.openai import OpenAIChatCompletionClient

from .utilities import *




def serialize_response(response):
    """Serialize the response object to a JSON-serializable format"""
    def convert_to_serializable(obj):
        if hasattr(obj, '__dict__'):
            # Convert objects with __dict__ to dictionaries
            result = {}
            for key, value in obj.__dict__.items():
                if not key.startswith('_'):  # Skip private attributes
                    result[key] = convert_to_serializable(value)
            return result
        elif isinstance(obj, (list, tuple)):
            return [convert_to_serializable(item) for item in obj]
        elif isinstance(obj, dict):
            return {key: convert_to_serializable(value) for key, value in obj.items()}
        elif isinstance(obj, datetime):
            return obj.isoformat()
        elif hasattr(obj, 'isoformat'):  # Handle other datetime-like objects
            return obj.isoformat()
        elif hasattr(obj, '__str__'):
            return str(obj)
        else:
            return obj
    
    return convert_to_serializable(response)


def extract_response_data(response):
    """Extract key information from the response for JSON output"""
    try:
        data = {
            "response_type": str(type(response)),
            "timestamp": datetime.now().isoformat(),
            "chat_message": None,
            "tool_calls": [],
            "tool_results": [],
            "content": None,
            "raw_response": None
        }
        
        # Extract chat message data
        if hasattr(response, 'chat_message') and response.chat_message:
            chat_msg = response.chat_message
            data["chat_message"] = {
                "id": getattr(chat_msg, 'id', None),
                "source": getattr(chat_msg, 'source', None),
                "type": getattr(chat_msg, 'type', None),
                "content": getattr(chat_msg, 'content', None),
                "created_at": getattr(chat_msg, 'created_at', None)
            }
            
            # Extract content
            if hasattr(chat_msg, 'content'):
                data["content"] = chat_msg.content
            
            # Extract tool calls
            if hasattr(chat_msg, 'tool_calls') and chat_msg.tool_calls:
                for tool_call in chat_msg.tool_calls:
                    tool_call_data = {
                        "id": getattr(tool_call, 'id', None),
                        "name": getattr(tool_call, 'name', None),
                        "arguments": getattr(tool_call, 'arguments', None)
                    }
                    data["tool_calls"].append(tool_call_data)
            
            # Extract tool results
            if hasattr(chat_msg, 'results') and chat_msg.results:
                for result in chat_msg.results:
                    result_data = {
                        "name": getattr(result, 'name', None),
                        "call_id": getattr(result, 'call_id', None),
                        "content": getattr(result, 'content', None),
                        "is_error": getattr(result, 'is_error', None)
                    }
                    data["tool_results"].append(result_data)
        
        # Store the full serialized response with selective Unicode decoding
        raw_response = serialize_response(response)
        data["raw_response"] = raw_response
        
        return data["raw_response"]
        
    except Exception as e:
        return {
            "error": f"Failed to extract response data: {str(e)}",
            "raw_response": str(response),
            "timestamp": datetime.now().isoformat()
        }


def get_all_functions_from_tools():
    """
    Scan the tools directory and extract all function names from Python files.
    
    Returns:
        list: List of all function names found in the tools directory
    """
    tools_dir = Path("tools")
    all_functions = []
    file_path_list = []
    
    if not tools_dir.exists():
        print("Error: tools directory not found!")
        return []
    
    # Iterate through all Python files in the tools directory
    for file_path in tools_dir.glob("*.py"):
        # Skip __init__.py
        if file_path.name == "__init__.py":
            continue
        file_path_list.append(file_path)
    
        # print(f"Scanning: {file_path}")
        # functions = extract_functions_from_file(file_path)
        # all_functions.extend(functions)
        
        # if functions:
        #    print(f"  Found functions: {functions}")
        # else:
        #    print(f"  No functions found")
    
    return file_path_list


async def generate_response(model, tasks_path, output_path, num):
    llm = ModelRegistry("configs/config.json").get(model)
    client = llm["client"]
    print(llm["name"])

    file_path_list = get_all_functions_from_tools()
    tools = []

    for file_path in file_path_list:
        server = StdioServerParams(
            command="python",
            args=[str(file_path)],
        )

        tools += await mcp_server_tools(server)
    print(tools)

    task_content = []
    tasks = load_data(tasks_path)
    for task in tasks:
        task_content.append(task["content"])


    # 构建工具定义列表
    tool_definitions = []
    if tools:
            for tool_func in tools:
                # 假设工具函数有标准的 docstring 作为描述
                # 格式: 函数名(参数): 描述
                docstring = (tool_func.schema["description"] or "这个工具没有提供描述。").strip()
                tool_definitions.append(f"- `{tool_func.schema['name']}`: {docstring}")

    tool_definitions_str = (
            "\n".join(tool_definitions) if tool_definitions else "无可用工具。"
        )

    # 创建一个内容更丰富的 system_message 模板
    system_message = f"""
You are a professional AI assistant, designed to use the provided tools to accurately and efficiently solve users’ problems.

Your task: Act according to the user’s request, following a fixed thinking process and response format.

**Thinking Process & Response Format:**

1. **Thought:**
   - First, you must carefully analyze the user’s needs and understand the core objective.
   - Formulate a clear, step-by-step plan to solve the problem, including selecting tools and their call parameters.
   - Before deciding the next action, you must clearly write your analysis, plan, and decision-making process in a text block that begins with `Thought:`. This section is for humans to read and is not the final answer.

2. **Tool Invocation:**
   - After outputting the `Thought:` block, if you need to call tools, directly use the registered function tools.
   - The system will automatically handle your tool-call requests.
   - When the task is complete, provide the user with a concise, complete final answer, and do not include the `Thought:` prefix anymore.

**Constraints:**
- **Strict constraint:** You must, and may only, choose tools from the “Available Tools List” below.
- **Invocation method:** Call the registered functions directly; do not output JSON or code-block descriptions.

**Available Tools List:**
{tool_definitions_str}

**Important Process:**
- Review the results returned by the tools.
- Reflect: You must reread the original task and your initial plan. Determine whether the task has been fully completed. If not, return to Step 1 and proceed with the next step in your plan. Do not provide the final answer until the task is fully complete.
- **Key reminder:** If the task involves multiple steps (e.g., first search for restaurants, then make a reservation), you must complete all steps. Do not stop after completing only part of the task.

Now, please begin working based on the user’s request. Be sure to include the `Thought:` section in your very first reply.
"""


    agent_construction_start = time.time()
    
    assistant = AssistantAgent(
        name="assistant",
        model_client=client,
        tools=tools,
        system_message=system_message,
        reflect_on_tool_use=True,
        max_tool_iterations=num, #the number of tools involved in your tasks
    
    )



    agent_construction_end = time.time()
    agent_construction_time = agent_construction_end - agent_construction_start

    all_responses = []

    task_processing_start = time.time()
    
    for i in range(len(task_content)):
        print(f"\n--- Processing Task {i+1}/{len(task_content)} ---")
        print(f"Task content: {task_content[i]}")
        
        try:
            response = await assistant.on_messages(
                [TextMessage(content=task_content[i], source="user")],
                cancellation_token=CancellationToken(),
            )

            response_data = extract_response_data(response)
            
            # Add task information to the response data
            response_data["task_index"] = i
            response_data["task_content"] = task_content[i]
            
            all_responses.append(response_data)
            
            print(f"Task {i+1} completed and added to responses")

            await assistant.on_reset(CancellationToken())
            
        except Exception as e:
            print(f"Error processing task {i+1}: {str(e)}")
            # Add error response to maintain consistency
            error_response = {
                "task_index": i,
                "task_content": task_content[i],
                "error": str(e),
                "timestamp": datetime.now().isoformat()
            }
            all_responses.append(error_response)

    task_processing_end = time.time()
    task_processing_time = task_processing_end - task_processing_start

    total_execution_time = task_processing_end - agent_construction_start
    
    timing_info = {"timing_info": {
        "agent_construction_time_seconds": agent_construction_time,
        "task_processing_time_seconds": task_processing_time,
        "total_execution_time_seconds": total_execution_time,
        "average_time_per_task_seconds": task_processing_time / len(task_content) if task_content else 0
    }}

    all_responses.append(timing_info)

    # Save all responses to JSON file with proper Unicode handling
    save_data(output_path, all_responses)

    
    print(f"\nAll response data saved to {output_path}")
    print(f"Total tasks processed: {len(all_responses) - 1}")
    print(f"File size: {os.path.getsize(output_path)} bytes")
