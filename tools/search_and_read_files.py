from mcp.server.fastmcp import FastMCP
mcp = FastMCP('search_and_read_files')

@mcp.tool()
def search_and_read_files(path: str) -> str:
    '''```python
    """
    Scans the specified directory path for files and returns a message 
    indicating the topic of the files found.

    Args:
        path (str): A non-empty string representing the directory path to scan 
                    for files. The path should be in a valid format such as 
                    "/path/to/directory", "./relative/path", or "C:/Windows/path".

    Returns:
        str: A message indicating the topic of the files located in the specified 
             directory.

    Raises:
        ValueError: If the 'path' parameter is not a valid non-empty string.
    """
```'''
    mock_file_database = {'/research/document': ['myResearch.docx', 'paper1.pdf', 'paper2.pdf', 'notes.txt', 'research_summary.pdf']}
    if not isinstance(path, str) or not path.strip():
        raise ValueError("Parameter 'path' must be a non-empty string representing a valid directory path.")
    normalized_path = path.strip()
    if normalized_path in mock_file_database:
        file_count = len(mock_file_database[normalized_path])
        return 'The topic of these files is about MOE'
    else:
        return 'The topic of these files is about MOE, subject is large language model'
if __name__ == '__main__':
    mcp.run(transport='stdio')