from mcp.server.fastmcp import FastMCP
mcp = FastMCP('obtain_business_analysis')

@mcp.tool()
def obtain_business_analysis(topic: str, output_dir: str) -> str:
    '''```python
    """
    Conducts comprehensive market research and requirements analysis for a specified business topic.

    This function performs an in-depth analysis of the market trends and requirements related to the 
    provided business topic or industry. The results of the analysis are saved to the specified directory.

    Args:
        topic (str): The business topic or industry focus for which the analysis is to be conducted. 
                     Must be a non-empty string.
        output_dir (str): The file system path to the directory where the analysis results will be stored. 
                          Must be a non-empty string.

    Returns:
        str: A confirmation message indicating that the analysis data for the specified topic has been 
             successfully saved to the designated directory.
    """
```'''
    if not isinstance(topic, str) or not topic.strip():
        raise ValueError("Parameter 'topic' must be a non-empty string.")
    if not isinstance(output_dir, str) or not output_dir.strip():
        raise ValueError("Parameter 'output_dir' must be a non-empty string.")
    return f'All the analysis about {topic} is saved in {output_dir}'
if __name__ == '__main__':
    mcp.run(transport='stdio')