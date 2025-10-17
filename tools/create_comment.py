from mcp.server.fastmcp import FastMCP
mcp = FastMCP('create_comment')

@mcp.tool()
def create_comment(id: str, comment: str) -> str:
    '''```python
    """
    Create a new comment on an existing Linear issue.

    Args:
        id (str): The unique identifier of the Linear issue. Must be a non-empty string.
        comment (str): The text of the comment to be added. Must be a non-empty string.

    Returns:
        str: A confirmation message indicating successful creation of the comment for the specified issue.
    """
```'''
    if not isinstance(id, str) or not id.strip():
        raise ValueError("Invalid 'id': must be a non-empty string representing the issue ID.")
    if not isinstance(comment, str) or not comment.strip():
        raise ValueError("Invalid 'comment': must be a non-empty string containing the comment text.")
    return f"Comment created successfully for issue '{id}'."
if __name__ == '__main__':
    mcp.run(transport='stdio')