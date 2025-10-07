from .utilities import *

"""
Tools listed in SKIP_INPUT_TOOLS will bypass expected input comparison during evaluation.
Populate this set with tool names for which input matching should be ignored.
"""
SKIP_INPUT_TOOLS: Set[str] = {
    # With extension
    "security_guidance",
    "download_osm_data",
    "search_news",
    "Execute_Database_Query",
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
    "UIUX_Expert"
}


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
    
    for i, (actual_input, expected_input, expected_tool) in enumerate(zip(inputs_used, expected_inputs, expected_tools)):
        # If any expected tool in this step is in the skip list, bypass input comparison
        try:
            expected_tool_names = list(expected_tool)
        except TypeError:
            expected_tool_names = [expected_tool]

        if any(tool_name in SKIP_INPUT_TOOLS for tool_name in expected_tool_names):
            continue

        if not compare_inputs(actual_input, expected_input):
            return 0
    
    return 1