from .utilities import *

"""
Tools listed in SKIP_INPUT_TOOLS will bypass expected input comparison during evaluation.
Populate this set with tool names for which input matching should be ignored.
"""
SKIP_INPUT_TOOLS: Set[str] = {
    # With extension
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
    "_3D_Game_Environment_Builder_generate_3d_assets",
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


def evaluate_task_performance(response_data: Dict[str, Any], expected_tools: List[str], expected_inputs: List[Dict[str, Any]]) -> int:
    """
    Evaluate a single task's performance.
    Returns 1 if both tools and inputs match exactly, 0 otherwise.
    """
    tools_used, inputs_used = extract_tools_and_inputs(response_data)

    # Normalize expected_tools so each step is a list of tool names
    normalized_expected_tools: List[List[str]] = []
    for tool_group in expected_tools:
        if isinstance(tool_group, (list, tuple)):
            normalized_expected_tools.append(list(tool_group))
        else:
            # Single tool provided as string
            normalized_expected_tools.append([tool_group])

    # Ensure number of steps match exactly
    if len(tools_used) != len(normalized_expected_tools):
        return 0

    # Check if tools match exactly (order of parallel tools in a step doesn't matter)
    for i, (actual_tool_group, expected_tool_group) in enumerate(zip(tools_used, normalized_expected_tools)):
        if set(actual_tool_group) != set(expected_tool_group):
            return 0

    # Normalize expected_inputs: allow flat list (one dict per tool call) or grouped per step
    expected_inputs_grouped: List[List[Dict[str, Any]]]
    if expected_inputs and all(isinstance(item, dict) for item in expected_inputs):
        # Flat list provided: group by the number of tools per step
        expected_inputs_grouped = []
        cursor = 0
        for expected_tool_group in normalized_expected_tools:
            group_size = len(expected_tool_group)
            group = expected_inputs[cursor:cursor + group_size]
            if len(group) != group_size:
                return 0
            expected_inputs_grouped.append(group)
            cursor += group_size
        # If there are leftover inputs, it's a mismatch
        if cursor != len(expected_inputs):
            return 0
    else:
        # Assume already grouped per step
        expected_inputs_grouped = expected_inputs  # type: ignore

    # Check if inputs match exactly per step
    if len(inputs_used) != len(expected_inputs_grouped):
        return 0

    for i, (actual_input, expected_input, expected_tool) in enumerate(zip(inputs_used, expected_inputs_grouped, normalized_expected_tools)):
        # If any expected tool in this step is in the skip list, bypass input comparison
        expected_tool_names = list(expected_tool)

        if any(tool_name in SKIP_INPUT_TOOLS for tool_name in expected_tool_names):
            continue

        if not compare_inputs(actual_input, expected_input):
            return 0
    
    return 1