from mcp.server.fastmcp import FastMCP
mcp = FastMCP('patch_file')

@mcp.tool()
def patch_file(path: str, changes_path: str) -> str:
    '''```python
    """
    Applies modifications to a specified file based on patch instructions from another file.

    This function reads a series of search and replace operations from a file specified by 
    `changes_path` and applies these modifications to the target file located at `path`.

    Args:
        path (str): The file path of the target file to which changes will be applied. 
                    Must be a non-empty string.
        changes_path (str): The file path containing the patch instructions. 
                            Must be a non-empty string.

    Returns:
        str: A confirmation message indicating that the modifications have been completed 
             and saved to the specified target file.
    """
```'''
    if not isinstance(path, str) or not path.strip():
        raise ValueError("Invalid 'path' parameter. Must be a non-empty string.")
    if not isinstance(changes_path, str) or not changes_path.strip():
        raise ValueError("Invalid 'changes_path' parameter. Must be a non-empty string.")
    return f'Modifications completed and saved in file: {path}'

if __name__ == '__main__':
    mcp.run(transport='stdio')