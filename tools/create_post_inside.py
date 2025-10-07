from mcp.server.fastmcp import FastMCP
mcp = FastMCP('create_post_inside')

@mcp.tool()
def create_post_inside(id: str, title: str, content: str, status: str, category: str, tags: list, date: str) -> str:
    '''```python
    """
    Creates a new post with the specified details.

    This function adds a new post to the collection if a post with the given 
    ID does not already exist. It validates the input parameters to ensure 
    they meet the required criteria.

    Args:
        id (str): A unique identifier for the post. Must be a non-empty string.
        title (str): The title of the post. Must be a non-empty string.
        content (str): The content of the post. Must be a non-empty string.
        status (str): The publication status of the post (e.g., 'draft', 'published'). 
                      Must be a non-empty string.
        category (str): The category under which the post is classified. 
                        Must be a non-empty string.
        tags (list): A list of tags associated with the post. Each tag must be a 
                     non-empty string.
        date (str): The date of creation or publication of the post. 
                    Must be a non-empty string.

    Returns:
        str: A confirmation message indicating the successful creation of the post 
             with its title, ID, category, and status.

    Raises:
        ValueError: If any of the required parameters ('id', 'title', 'content', 
                    'status', 'category', 'date') are not non-empty strings, 
                    or if 'tags' is not a list, or if a post with the given ID 
                    already exists.
    """
```'''
    if not hasattr(create_post_inside, 'mock_db'):
        create_post_inside.mock_db = {'posts': []}
    required_params = {'id': id, 'title': title, 'content': content, 'status': status, 'category': category, 'date': date}
    for (param_name, param_value) in required_params.items():
        if not isinstance(param_value, str) or not param_value.strip():
            raise ValueError(f"Parameter '{param_name}' is required and must be a non-empty string.")
    if not isinstance(tags, list):
        raise ValueError("Parameter 'tags' must be a list.")
    existing_post = next((p for p in create_post_inside.mock_db['posts'] if p['id'] == id), None)
    if existing_post:
        raise ValueError(f"A post with id '{id}' already exists.")
    new_post = {'id': id, 'title': title.strip(), 'content': content.strip(), 'status': status.strip().lower(), 'category': category.strip(), 'tags': [tag.strip() for tag in tags if isinstance(tag, str) and tag.strip()], 'date': date.strip()}
    create_post_inside.mock_db['posts'].append(new_post)
    return f"Post '{new_post['title']}' (ID: {new_post['id']}) successfully created in category '{new_post['category']}' with status '{new_post['status']}'."
if __name__ == '__main__':
    mcp.run(transport='stdio')