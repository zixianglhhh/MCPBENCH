from mcp.server.fastmcp import FastMCP
mcp = FastMCP('meshi_doko')

@mcp.tool()
def meshi_doko(LOCATION: str, BUDGET: int, query: str, conversation_id: int) -> str:
    '''```python
    """
    Provides restaurant recommendations by interfacing with Dify AI based on location, budget, and query.

    Args:
        LOCATION (str): The location where the restaurant is sought. Must be a non-empty string.
        BUDGET (int): The maximum budget in yen for the restaurant. Must be a positive integer.
        query (str): Keywords describing the type of restaurant or food desired. Must be a non-empty string.
        conversation_id (int): An integer identifier for maintaining conversation context.

    Returns:
        str: A formatted string containing restaurant recommendations that match the given criteria,
        or a message indicating no matches were found. Includes the conversation ID for context.
    """
```'''
    mock_restaurants = [{'name': 'Light Snack Heaven', 'location': 'Tokyo', 'budget_range': (500, 1500), 'type': 'light snacks', 'description': 'A cozy spot famous for its sandwiches, salads, and fresh juices.'}, {'name': 'Snack & Chat', 'location': 'Tokyo', 'budget_range': (800, 2000), 'type': 'light snacks', 'description': 'Trendy café with small plates, tapas, and light meals perfect for quick meetings.'}, {'name': 'Salalad House', 'location': 'Osaka', 'budget_range': (700, 1800), 'type': 'salad specialty', 'description': 'A popular salad restaurant known for its fresh vegetables and unique dressings.'}, {'name': 'The Bento Corner', 'location': 'Kyoto', 'budget_range': (600, 1200), 'type': 'light snacks', 'description': 'Serving traditional Japanese bento with a modern twist.'}, {'name': 'Evening Bites', 'location': 'Tokyo', 'budget_range': (1000, 3000), 'type': 'light snacks', 'description': 'Small yet elegant restaurant offering an array of evening light meals.'}]
    if not isinstance(LOCATION, str) or not LOCATION.strip():
        raise ValueError('LOCATION must be a non-empty string.')
    if not isinstance(BUDGET, int) or BUDGET <= 0:
        raise ValueError('BUDGET must be a positive integer.')
    if not isinstance(query, str) or not query.strip():
        raise ValueError('query must be a non-empty string.')
    if not isinstance(conversation_id, int):
        raise ValueError('conversation_id must be an integer.')
    query_lower = query.lower()
    matched_restaurants = []
    for restaurant in mock_restaurants:
        if restaurant['location'].lower() == LOCATION.lower() and restaurant['budget_range'][0] <= BUDGET <= restaurant['budget_range'][1] and any((keyword in restaurant['type'].lower() or keyword in restaurant['name'].lower() for keyword in query_lower.split())):
            matched_restaurants.append(restaurant)
    if not matched_restaurants:
        return f"Sorry, I couldn't find any restaurants in {LOCATION} within your budget of {BUDGET} yen matching your query '{query}'."
    response_lines = [f'Here are some restaurant recommendations in {LOCATION} within your budget of {BUDGET} yen:']
    for r in matched_restaurants:
        response_lines.append(f"- {r['name']}: {r['description']} (Type: {r['type']}, Budget range: {r['budget_range'][0]}–{r['budget_range'][1]} yen)")
    response_lines.append(f'[Conversation ID: {conversation_id} maintained for context]')
    return '\n'.join(response_lines)
if __name__ == '__main__':
    mcp.run(transport='stdio')