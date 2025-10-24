from mcp.server.fastmcp import FastMCP
mcp = FastMCP('WebSearchConfig')

@mcp.tool()
def WebSearchConfig(name: str, description: str, search_engine: str, max_results: str, extract_content: str) -> str:
    '''```python
    """
    Configures the web search tool with specified parameters.

    This function sets up a web search configuration using the provided
    parameters such as the name, description, search engine, maximum number
    of results, and content extraction preference. It validates the input
    parameters and returns a confirmation message upon successful configuration.

    Args:
        name (str): The name of the web search configuration. Must be a non-empty string, must be one of [Default Web Search, Nearby Restaurants Search].
        description (str): A brief description of the web search configuration. Must be a non-empty string.
        search_engine (str): The search engine to be used (e.g., 'Google'). Must be a non-empty string.
        max_results (str): The maximum number of search results to return. Must be a non-empty string containing digits only.
        extract_content (str): A flag indicating whether to extract content ('true' or 'false'). Must be one of these strings.

    Returns:
        str: A message confirming the successful creation of the web search configuration.
    """
```'''
    mock_config_db = {'Nearby Restaurants Search': {'name': 'Nearby Restaurants Search', 'description': 'Search for restaurants near the current location based on user preferences.', 'search_engine': 'Google', 'max_results': '20', 'extract_content': 'true', 'url': 'https://maps.google.com/search/restaurants'}, 'Default Web Search': {'name': 'Default Web Search', 'description': 'General web search configuration for various purposes.', 'search_engine': 'Google', 'max_results': '10', 'extract_content': 'false', 'url': 'https://google.com/defaultsearch'}}
    if not isinstance(name, str) or not name.strip():
        raise ValueError("Parameter 'name' must be a non-empty string.")
    if not isinstance(description, str) or not description.strip():
        raise ValueError("Parameter 'description' must be a non-empty string.")
    if not isinstance(search_engine, str) or not search_engine.strip():
        raise ValueError("Parameter 'search_engine' must be a non-empty string.")
    if not isinstance(max_results, str) or not max_results.strip() or (not max_results.isdigit()):
        raise ValueError("Parameter 'max_results' must be a non-empty string containing digits only.")
    if not isinstance(extract_content, str) or extract_content.lower() not in ['true', 'false']:
        raise ValueError("Parameter 'extract_content' must be a string 'true' or 'false'.")
    config_key = name.strip()
    mock_config_db[config_key] = {'name': name.strip(), 'description': description.strip(), 'search_engine': search_engine.strip(), 'max_results': max_results.strip(), 'extract_content': extract_content.strip().lower(), 'url': f'https://maps.google.com/search/restaurants' if 'restaurant' in description.lower() or 'restaurants' in description.lower() else 'https://google.com/defaultsearch'}
    if 'restaurant' in description.lower() or 'restaurants' in description.lower():
        response_msg = f"Web search configuration '{name}' has been set up to use {search_engine} engine, returning up to {max_results} results, with content extraction set to {extract_content}, the deployed url is {mock_config_db[config_key]['url']}. This configuration is optimized for finding nearby restaurants."
    else:
        response_msg = f"Web search configuration '{name}' successfully created with {search_engine} engine and max {max_results} results (extract_content={extract_content}) and the deployed url is {mock_config_db[config_key]['url']}."
    return response_msg
if __name__ == '__main__':
    mcp.run(transport='stdio')