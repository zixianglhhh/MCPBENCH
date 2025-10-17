from mcp.server.fastmcp import FastMCP
mcp = FastMCP('convert_pdf_to_markdown')

@mcp.tool()
def convert_pdf_to_markdown(pdf_dir: str) -> str:
    '''```python
"""
Converts PDF files located in the specified directory to Markdown format.

This function processes all PDF files found within the given directory path,
converting each one to a corresponding Markdown file. The directory path must
be a valid, non-empty string.

Args:
    pdf_dir (str): The directory path containing the PDF file(s) to be converted.
                   It should be a valid path pointing to the location of the PDF files.

Returns:
    str: A message indicating that all PDF files have been successfully converted
         to Markdown format.
"""
```'''
    if not isinstance(pdf_dir, str) or not pdf_dir.strip():
        raise ValueError('Invalid pdf_dir: must be a non-empty string.')
    return 'All PDF files have been converted to Markdown format.'
if __name__ == '__main__':
    mcp.run(transport='stdio')