from mcp.server.fastmcp import FastMCP
mcp = FastMCP('create_task')

@mcp.tool()
def create_task(title: str, description: str, dueDate: str, priority: int) -> str:
    '''```python
"""
Creates a new task in TickTick with specified details.

This function allows you to create a task by providing essential information such as the title, description, due date, and priority level. It validates the input parameters to ensure they meet the required formats and constraints.

Args:
    title (str): The title of the task. Must be a non-empty string.
    description (str): The content or description of the task. Optional; if provided, must be a string.
    dueDate (str): The due date for the task. Optional; if provided, must be a string.
    priority (int): The priority level of the task, ranging from 0 (lowest) to 3 (highest). Must be an integer within this range.

Returns:
    str: A confirmation message indicating the successful creation of the task, or an error message if validation fails.
"""
```'''
    if not isinstance(title, str) or not title.strip():
        return "Error: 'title' must be a non-empty string."
    if description is not None and (not isinstance(description, str)):
        return "Error: 'description' must be a string if provided."
    if dueDate is not None and (not isinstance(dueDate, str)):
        return "Error: 'dueDate' must be a string if provided."
    if priority is not None:
        if not isinstance(priority, int) or priority < 0 or priority > 3:
            return "Error: 'priority' must be an integer between 0 and 3."
    return f"Task '{title}' has been created successfully."
if __name__ == '__main__':
    mcp.run(transport='stdio')