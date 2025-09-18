import json
from typing import List, Dict, Any, Set

def load_data(file_path: str) -> List[Dict[str, Any]]:
    """Load data from JSON file."""
    with open(file_path, 'r', encoding='utf-8') as f:
        return json.load(f)

def save_data(file_path: str, data) -> None:
    """Save data to JSON file."""
    with open(file_path, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=2)
        print (f"Data saved to {file_path}!")

def extract_tools_and_inputs(response_data: Dict[str, Any]) -> tuple[List[List[str]], List[List[Dict[str, Any]]]]:
    """
    Extract tool calls and their inputs from a single response.
    Returns a tuple of (tools, inputs), where each group contains called tools/inputs.
    """
    tools = []
    inputs = []
    
    # Check inner_messages for ToolCallRequestEvent
    if 'inner_messages' in response_data:
        for message in response_data['inner_messages']:
            if message.get('type') == 'ToolCallRequestEvent':
                if 'content' in message and isinstance(message['content'], list):
                    # Extract all tools and inputs called in this single event (parallel execution)
                    tools_in_one_call = []
                    inputs_in_one_call = []
                    for tool_call in message['content']:
                        if 'name' in tool_call:
                            tools_in_one_call.append(tool_call['name'])
                            # Extract arguments
                            if 'arguments' in tool_call:
                                try:
                                    args = json.loads(tool_call['arguments'])
                                    inputs_in_one_call.append(args)
                                except json.JSONDecodeError:
                                    inputs_in_one_call.append({})
                            else:
                                inputs_in_one_call.append({})
                    
                    tools.append(tools_in_one_call)
                    inputs.append(inputs_in_one_call)
    
    return tools, inputs

def compare_inputs(actual_input, expected_input) -> bool:
    """
    Compare actual input with expected input.
    Returns True if they match, False otherwise.
    Parameter order within each input set does not matter.
    """
    # Convert values to strings for comparison to handle type differences
    def normalize_dict(d):
        return {k: str(v) for k, v in d.items()}

    actual_input = [normalize_dict(input) for input in actual_input]
    expected_input = [normalize_dict(input) for input in expected_input]

    actual_input_set = {frozenset(d.items()) for d in actual_input}
    expected_input_set = {frozenset(d.items()) for d in expected_input}
    
    # Compare the normalized dictionaries
    return actual_input_set == expected_input_set




