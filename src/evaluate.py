from .utilities import *


def evaluate_task_performance(response_data: Dict[str, Any], expected_tools: List[str], expected_inputs: List[Dict[str, Any]]) -> int:
    """
    Evaluate a single task's performance.
    Returns 1 if both tools and inputs match exactly, 0 otherwise.
    """
    tools_used, inputs_used = extract_tools_and_inputs(response_data)
    
    # Check if tools match exactly (including order)
    for i, (actual_tool, expected_tool) in enumerate(zip(tools_used, expected_tools)):
        if set(actual_tool) != set(expected_tool):
            return 0
    
    # Check if inputs match exactly
    if len(inputs_used) != len(expected_inputs):
        return 0
    
    for i, (actual_input, expected_input) in enumerate(zip(inputs_used, expected_inputs)):
        if not compare_inputs(actual_input, expected_input):
            return 0
    
    return 1