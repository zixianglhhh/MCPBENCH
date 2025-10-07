from mcp.server.fastmcp import FastMCP
from typing import List
mcp = FastMCP('create_post_cross_media')

@mcp.tool()
def create_post_cross_media(instruction_dir: str, platforms: List[str], postImmediately: bool) -> str:
    '''```python
    """
    Create and post content across multiple social media platforms.

    This function reads post requirements from a specified directory and facilitates 
    the creation and distribution of social media posts by allowing users to select 
    target platforms and choose whether to schedule or immediately publish the content. 
    It returns the status of the post creation and publication process, indicating 
    success or failure.

    Args:
        instruction_dir (str): The directory path containing all the requirements 
            and content specifications for the post. Must be a non-empty string 
            representing a valid directory path, such as "/content/posts/charity_race" 
            or "./post_requirements".
        platforms (List[str]): A list of target social media platforms where 
            the content should be posted. Each platform must be a string.
        postImmediately (bool): A boolean flag indicating whether the post 
            should be published immediately (True) or scheduled for later 
            (False).

    Returns:
        str: A message indicating the result of the post creation and 
        publication process, including any special notes if applicable.
    """
```'''
    # Basic input validation
    if not isinstance(instruction_dir, str) or not instruction_dir.strip():
        return "Error: 'instruction_dir' must be a non-empty string representing a valid directory path."
    if not isinstance(platforms, list) or not all((isinstance(p, str) for p in platforms)):
        return "Error: 'platforms' must be a list of strings."
    if not isinstance(postImmediately, bool):
        return "Error: 'postImmediately' must be a boolean value."
    
    # Mock supported platforms
    supported_platforms = {'facebook', 'twitter', 'instagram', 'linkedin', 'mastodon'}
    invalid_platforms = [p for p in platforms if p.lower() not in supported_platforms]
    if invalid_platforms:
        return f"Error: Unsupported platforms requested: {', '.join(invalid_platforms)}"
    
    # Mock the post creation and publishing process
    if 'charity race' in instruction_dir.lower() and any((p in ['facebook', 'twitter', 'instagram'] for p in platforms)):
        special_note = 'Campaign prepared for charity race promotion with trending hashtags.'
    else:
        special_note = 'Content prepared from directory requirements as requested.'
    
    if postImmediately:
        return f"Post created and published immediately on: {', '.join(platforms)}. {special_note}"
    else:
        return f"Post created and scheduled for: {', '.join(platforms)}. {special_note}"
if __name__ == '__main__':
    mcp.run(transport='stdio')