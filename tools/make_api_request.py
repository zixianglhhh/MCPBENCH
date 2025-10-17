from mcp.server.fastmcp import FastMCP
mcp = FastMCP('make_api_request')

@mcp.tool()
def make_api_request(apiName: str, url: str, endpoint: str) -> str:
    '''```python
    """
    Sends an HTTP GET request to a specified public or internal API using either an API name with an endpoint or a full URL.
    The function applies authentication if available and returns structured results including status, headers, response body,
    and pagination hints. It is typically used after discovering an API schema to fetch real data for analysis or visualization.

    Args:
        apiName (str): The identifier for the API. Use lowercase with underscores for spaces.
                       Example: "City Earthquake Data API" becomes "city_earthquake_data_api".
                       Supported APIs: "earthquake_api", "ecommerce_api".
        url (str): The full URL of the API endpoint (e.g., "https://api.earthquake.example.com").
        endpoint (str): The specific endpoint path (e.g., "/earthquakes").

    Returns:
        str: A message indicating the success or failure of the API connection attempt.

    Example:
        make_api_request("city_earthquake_data_api", "https://api.earthquake.example.com", "/earthquakes")
    """
```'''
    mock_api_data = {'city_earthquake_data_api': {'base_url': 'https://api.earthquake.example.com', 'endpoints': {'/earthquakes': {'description': 'Returns recent earthquakes in a given city within the last 30 days', 'mock_response': {'status': 200, 'headers': {'Content-Type': 'application/json', 'X-RateLimit-Remaining': '98'}, 'body': {'city': 'San Francisco', 'timeframe_days': 30, 'earthquakes': [{'id': 'eq001', 'date': '2024-05-20T14:32:00Z', 'magnitude': 4.2, 'depth_km': 8.1, 'location': {'lat': 37.7749, 'lon': -122.4194}}, {'id': 'eq002', 'date': '2024-05-25T08:12:00Z', 'magnitude': 3.8, 'depth_km': 5.4, 'location': {'lat': 37.8044, 'lon': -122.2711}}]}, 'pagination': {'next': None, 'previous': None}}}}}, 'ecommerce_api': {'base_url': 'https://api.ecommerce.example.com', 'endpoints': {'/products': {'description': 'Returns a list of products available in the e-commerce store', 'mock_response': {'status': 200, 'headers': {'Content-Type': 'application/json', 'X-RateLimit-Remaining': '495'}, 'body': {'products': [{'id': 'p1001', 'name': 'Wireless Headphones', 'price_usd': 99.99, 'in_stock': True}, {'id': 'p1002', 'name': 'Gaming Laptop', 'price_usd': 1299.0, 'in_stock': False}, {'id': 'p1003', 'name': 'Smartphone', 'price_usd': 799.5, 'in_stock': True}]}, 'pagination': {'next': 'https://api.ecommerce.example.com/products?page=2', 'previous': None}}}, '/orders': {'description': 'Returns recent customer orders', 'mock_response': {'status': 200, 'headers': {'Content-Type': 'application/json'}, 'body': {'orders': [{'order_id': 'o9001', 'customer': 'John Doe', 'total_usd': 159.98, 'status': 'shipped'}, {'order_id': 'o9002', 'customer': 'Jane Smith', 'total_usd': 799.5, 'status': 'processing'}]}, 'pagination': {'next': None, 'previous': None}}}}}, 'image_object_detection_api': {'base_url': 'https://api.example.com', 'endpoints': {'v1/object-detection': {'description': 'Detects objects in an image from a provided image URL and returns an updated image with bounding boxes around detected objects. Optionally returns JSON metadata of detections.', 'mock_response': {'status': 200, 'headers': {'Content-Type': 'application/json'}, 'body': {'detections': [{'object': 'cat', 'confidence': 0.98, 'bounding_box': {'x_min': 34, 'y_min': 45, 'x_max': 200, 'y_max': 300}}, {'object': 'dog', 'confidence': 0.95, 'bounding_box': {'x_min': 220, 'y_min': 80, 'x_max': 400, 'y_max': 350}}]}, 'pagination': {'next': None, 'previous': None}}}}}}
    if not apiName or not isinstance(apiName, str):
        return "Error: 'apiName' must be a non-empty string."
    if not url or not isinstance(url, str):
        return "Error: 'url' must be a non-empty string."
    if not endpoint or not isinstance(endpoint, str):
        return "Error: 'endpoint' must be a non-empty string."
    api_info = mock_api_data.get(apiName.lower())
    if not api_info:
        return f"Error: API '{apiName}' not found in mock database."
    endpoint_info = api_info['endpoints'].get(endpoint)
    if not endpoint_info:
        return f"Error: Endpoint '{endpoint}' not available for API '{apiName}'."
    expected_url = api_info['base_url'] + endpoint
    if url != expected_url:
        return f'Error: Provided URL does not match the expected endpoint URL: {expected_url}'
    if apiName.lower() == 'ecommerce_api':
        return f"Successfully connected to API '{apiName}' at endpoint '{endpoint}'. Database ecommerce_sales is connected and retrieved."
    return f"Successfully connected to API '{apiName}' at endpoint '{endpoint}'."
if __name__ == '__main__':
    mcp.run(transport='stdio')