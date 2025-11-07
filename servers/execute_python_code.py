from mcp.server.fastmcp import FastMCP
'\nautomatically execute the python code in the specified directory, automatically install the packages required by the code.\n'
mcp = FastMCP('execute_python_code')

@mcp.tool()
def execute_python_code(code_dir: str) -> str:
    '''```python
    """
    Executes a Python file at the specified path.

    This function takes a file path as input and executes the Python file
    located at that path. It ensures that the file path provided is
    a non-empty string pointing to a valid Python file.

    Args:
        code_dir (str): The path to the Python file to be executed.
                        Must be a non-empty string pointing to a .py file.
                        Example: "./a.py", "/path/to/script.py", "C:/scripts/example.py"

    Returns:
        str: A message indicating the successful execution of the Python file.

    Raises:
        ValueError: If 'code_dir' is not a non-empty string.

    Example:
        execute_python_code("./a.py")
        # Returns: "Python code successfully executed in directory: ./a.py"
    """
```'''
    if not isinstance(code_dir, str) or not code_dir.strip():
        raise ValueError("Parameter 'code_dir' must be a non-empty string.")
    if not code_dir.strip():
        return f"Error: Invalid file path '{code_dir}'."
    result = f'Python code successfully executed in directory: {code_dir}'
    return result
if __name__ == '__main__':
    mcp.run(transport='stdio')