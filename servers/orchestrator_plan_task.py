from mcp.server.fastmcp import FastMCP
from typing import List
mcp = FastMCP('orchestrator_plan_task')

@mcp.tool()
def orchestrator_plan_task(topic: str, scope: str, schedule: str, constraints: List[str], dependencies: List[str]) -> str:
    '''```python
    """
    Generates a detailed task breakdown for orchestrating a data pipeline.

    This function creates a structured plan for executing a data pipeline
    based on the provided topic, scope, schedule, constraints, and dependencies.
    It returns a formatted string summarizing the task plan, including the
    breakdown of steps required to achieve the specified objectives.

    Args:
        topic (str): The specific topic or name of the data pipeline. Determines
            if a predefined plan is available.
        scope (str): A description of the scope of the task. Must be a non-empty string.
        schedule (str): The schedule in cron format for executing the task. Must be a non-empty string.
        constraints (List[str]): A list of constraints that must be considered during planning.
            Must be a non-empty list of strings.
        dependencies (List[str]): A list of dependencies that affect the task execution.
            Must be a non-empty list of strings.

    Returns:
        str: A formatted string summarizing the task plan, including the scope,
        schedule, constraints, dependencies, and a step-by-step breakdown of tasks.
    """
```'''
    if not scope or not isinstance(scope, str):
        raise ValueError("Parameter 'scope' is required and must be a non-empty string.")
    if not schedule or not isinstance(schedule, str):
        raise ValueError("Parameter 'schedule' is required and must be a non-empty string.")
    if not isinstance(constraints, list) or not constraints:
        raise ValueError("Parameter 'constraints' is required and must be a non-empty list.")
    if not isinstance(dependencies, list) or not dependencies:
        raise ValueError("Parameter 'dependencies' is required and must be a non-empty list.")
    mock_plans = {'Zoho & Pipedrive to BigQuery pipeline': [{'step': 1, 'task': 'Extract data from Zoho Invoice API and Pipedrive API', 'notes': 'Data extraction is assumed to be complete based on scope.'}, {'step': 2, 'task': 'Clean raw data', 'notes': 'Standardize date formats, remove duplicates, handle null values.'}, {'step': 3, 'task': 'Integrate datasets', 'notes': 'Join financial and sales data on customer/company IDs.'}, {'step': 4, 'task': 'Load integrated data into Google BigQuery', 'notes': 'Respect schema consistency and privacy rules.'}, {'step': 5, 'task': 'Run provided SQL queries', 'notes': 'Execute analysis SQL already provided and verify output.'}]}
    if topic and topic in mock_plans:
        plan_steps = mock_plans[topic]
    else:
        plan_steps = [{'step': 1, 'task': 'Define data sources and confirm data extraction readiness', 'notes': 'Clarify any assumptions from constraints.'}, {'step': 2, 'task': 'Perform data cleaning and transformation', 'notes': 'Ensure data quality, enforce privacy constraints.'}, {'step': 3, 'task': 'Integrate datasets as per scope requirements', 'notes': 'Consider dependencies for upstream/downstream tasks.'}, {'step': 4, 'task': 'Load final dataset to target destination', 'notes': 'Match loading schedule to given cadence.'}]
    plan_summary = f"Task Plan for: {topic or 'Generic Data Pipeline'}\n"
    plan_summary += f'Scope: {scope}\n'
    plan_summary += f'Schedule (cron): {schedule}\n'
    plan_summary += 'Constraints:\n'
    for c in constraints:
        plan_summary += f'  - {c}\n'
    plan_summary += 'Dependencies:\n'
    for d in dependencies:
        plan_summary += f'  - {d}\n'
    plan_summary += '\nBreakdown:\n'
    for step in plan_steps:
        plan_summary += f"Step {step['step']}: {step['task']} ({step['notes']})\n"
    return plan_summary
if __name__ == '__main__':
    mcp.run(transport='stdio')