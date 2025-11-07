from .utilities import *


def evaluate_task_performance(response_data: Dict[str, Any], expected_tools: List[List[str]], expected_inputs: List[List[Dict[str, Any]]], num_expected_tools: int) -> int:
    """
    Evaluate a single task's performance.
    Returns 1 * num_expected_tools (i.e give different weights to tasks with different number of expected tools) if both tools and inputs match exactly, 0 otherwise.
    """

    # Tools to skip when comparing inputs
    SKIP_INPUT_TOOLS: Set[str] = {
        "security_guidance",
        "search_news",
        "vector_search",
        "search_papers",
        "meshi_doko",
        "execute_bigquery",
        "search_academic_papers",
        "wolfram_query",
        "search_pubmed",
        "analyze_trends",
        "get_posts",
        "orchestrator_plan_task",
        "obtain_business_analysis",
        "generate_code",
        "system_architecture_designer",
        "UIUX_Expert",
        "generate_3d_assets",
        "strategy_guide",
        "create_ui",
        "dmagent_ask_narrative",
        "dmagent_ask_rule",
        "diceRoll",
        'Tester',
        'system_architecture_designer',
        "search_academic_papers",
        "generate_code",
        "execute_python_code"
    }

    tools_used, inputs_used = extract_tools_and_inputs(response_data)
    
    # Check if tools match exactly (including order in different toolcallrequest steps)
    for i, (actual_tool, expected_tool) in enumerate(zip(tools_used, expected_tools)):
        if set(actual_tool) != set(expected_tool):
            return 0

    # Check if inputs length match exactly
    if len(inputs_used) != len(expected_inputs):
        return 0
    
    for i, (actual_inputs_step, expected_inputs_step) in enumerate(zip(inputs_used, expected_inputs)):
        # Get the tools for this step
        expected_tool_names_in_step = expected_tools[i]
        actual_tool_names_in_step = tools_used[i]
        
        # Create list of (tool_name, input) pairs to handle duplicate tool names
        expected_tool_input_pairs = [
            (tool_name, expected_inputs_step[j])
            for j, tool_name in enumerate(expected_tool_names_in_step)
            if j < len(expected_inputs_step)
        ]
        
        actual_tool_input_pairs = [
            (tool_name, actual_inputs_step[j])
            for j, tool_name in enumerate(actual_tool_names_in_step)
            if j < len(actual_inputs_step)
        ]
        
        # Filter out inputs for tools in the skip list
        filtered_expected_inputs = [
            input_data
            for tool_name, input_data in expected_tool_input_pairs
            if tool_name not in SKIP_INPUT_TOOLS
        ]
        
        filtered_actual_inputs = [
            input_data
            for tool_name, input_data in actual_tool_input_pairs
            if tool_name not in SKIP_INPUT_TOOLS
        ]
        
        # Compare filtered inputs (only for tools not in skip list)
        if filtered_actual_inputs or filtered_expected_inputs:
            if not compare_inputs(filtered_actual_inputs, filtered_expected_inputs):
                return 0

    score = 1 * num_expected_tools

    return score
