from mcp.server.fastmcp import FastMCP
mcp = FastMCP('get_posts')

@mcp.tool()
def get_posts(topic: str, order: str, count: int, featured: str, posted_before: str, posted_after: str) -> str:
    '''```python
    """
    Retrieves a list of posts filtered by specified criteria.

    This function fetches posts based on the provided topic, order, count, 
    featured status, and date range. It returns a formatted string of posts 
    that match the given filters.

    Args:
        topic (str): The topic to filter posts by. Must be a non-empty string.
        order (str): The order in which to sort posts. Accepts 'asc' for 
            ascending or 'desc' for descending.
        count (int): The maximum number of posts to return. Must be a positive 
            integer.
        featured (str): Filter posts based on featured status. Accepts 'yes', 
            'no', or 'any'.
        posted_before (str): The upper date limit for posts, in 'YYYY-MM-DD' 
            format.
        posted_after (str): The lower date limit for posts, in 'YYYY-MM-DD' 
            format.

    Returns:
        str: A formatted string of posts matching the specified criteria, 
        including post ID, title, posted date, and featured status. Returns an 
        error message if input validation fails or 'No posts found matching 
        the given criteria.' if no posts match the filters.
    """
```'''
    mock_posts_db = [{'id': 1, 'title': 'Album Review: The Eternal Echoes', 'topic': 'music', 'content': "A deep dive into the ambient soundscapes of 'The Eternal Echoes'.", 'featured': 'yes', 'posted_date': '2024-05-10', 'order_rank': 5}, {'id': 2, 'title': 'Top 10 Indie Rock Albums of 2023', 'topic': 'music', 'content': 'Counting down the most influential indie rock albums released in 2023.', 'featured': 'no', 'posted_date': '2024-01-15', 'order_rank': 4}, {'id': 3, 'title': 'Concert Review: Symphony Under the Stars', 'topic': 'music', 'content': 'An enchanting evening of orchestral classics performed outdoors.', 'featured': 'yes', 'posted_date': '2023-11-05', 'order_rank': 3}, {'id': 4, 'title': 'Guide to Building a Home Recording Studio', 'topic': 'music', 'content': 'Tips and tricks to set up your own music recording space at home.', 'featured': 'no', 'posted_date': '2023-08-22', 'order_rank': 2}, {'id': 5, 'title': 'New Jazz Horizons: Emerging Artists to Watch', 'topic': 'music', 'content': 'Profiling the next generation of jazz musicians pushing the genre forward.', 'featured': 'yes', 'posted_date': '2024-03-30', 'order_rank': 1}]
    from datetime import datetime
    if not isinstance(topic, str) or not topic.strip():
        return "Error: 'topic' must be a non-empty string."
    if not isinstance(order, str) or order.lower() not in ['asc', 'desc']:
        return "Error: 'order' must be 'asc' or 'desc'."
    if not isinstance(count, int) or count <= 0:
        return "Error: 'count' must be a positive integer."
    if not isinstance(featured, str) or featured.lower() not in ['yes', 'no', 'any']:
        return "Error: 'featured' must be 'yes', 'no', or 'any'."
    try:
        posted_before_dt = datetime.strptime(posted_before, '%Y-%m-%d')
        posted_after_dt = datetime.strptime(posted_after, '%Y-%m-%d')
    except ValueError:
        return "Error: 'posted_before' and 'posted_after' must be in 'YYYY-MM-DD' format."
    filtered_posts = [p for p in mock_posts_db if p['topic'].lower() == topic.lower()]
    if featured.lower() != 'any':
        filtered_posts = [p for p in filtered_posts if p['featured'].lower() == featured.lower()]
    filtered_posts = [p for p in filtered_posts if datetime.strptime(p['posted_date'], '%Y-%m-%d') < posted_before_dt and datetime.strptime(p['posted_date'], '%Y-%m-%d') > posted_after_dt]
    reverse_order = True if order.lower() == 'desc' else False
    filtered_posts.sort(key=lambda x: x['order_rank'], reverse=reverse_order)
    filtered_posts = filtered_posts[:count]
    if not filtered_posts:
        return 'No posts found matching the given criteria.'
    result_lines = []
    for post in filtered_posts:
        line = f"[{post['id']}] {post['title']} ({post['posted_date']}) - Featured: {post['featured']}"
        result_lines.append(line)
    return '\n'.join(result_lines)
if __name__ == '__main__':
    mcp.run(transport='stdio')