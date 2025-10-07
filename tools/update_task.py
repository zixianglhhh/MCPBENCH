from mcp.server.fastmcp import FastMCP
mcp = FastMCP('update_task')

@mcp.tool()
def update_task(task_id: str, task_name: str, content: str, dueDate: str, priority: int) -> str:
    '''```python
"""
Updates an existing task in TickTick with new details.

This function allows you to modify an existing task's name, content, due date, and priority level in the TickTick task management system.

Args:
    task_id (str): The unique identifier of the task to be updated. Must be a non-empty string.
    task_name (str): The new name for the task. If provided, must be a string.
    content (str): The new content or description for the task. If provided, must be a string.
    dueDate (str): The new due date for the task. If provided, must be a string.
    priority (int): The new priority level for the task, ranging from 0 (lowest) to 3 (highest). Must be an integer within this range.

Returns:
    str: A confirmation message indicating that the task has been successfully updated.
"""
```'''
    if not isinstance(task_id, str) or not task_id.strip():
        return "Error: 'task_id' must be a non-empty string."
    if task_name is not None and (not isinstance(task_name, str)):
        return "Error: 'task_name' must be a string if provided."
    if content is not None and (not isinstance(content, str)):
        return "Error: 'content' must be a string if provided."
    if dueDate is not None and (not isinstance(dueDate, str)):
        return "Error: 'dueDate' must be a string if provided."
    if priority is not None:
        if not isinstance(priority, int) or priority < 0 or priority > 3:
            return "Error: 'priority' must be an integer between 0 and 3."
    return f"Task '{task_id}' has been updated successfully."
if __name__ == '__main__':
    mcp.run(transport='stdio')