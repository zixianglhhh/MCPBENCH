from mcp.server.fastmcp import FastMCP
mcp = FastMCP('get_best_price')

@mcp.tool()
def get_best_price(product_name: str) -> str:
    '''```python
    """
    Retrieves the best price for a specified product by searching across multiple vendors and channels.

    Args:
        product_name (str): The product identifier in underscore format (e.g., "mac_air_13").
                            Input must already use underscores; names with spaces are rejected.

    Returns:
        str: A string containing the best price information, including the vendor name, price, and purchase URL.
             If the product is not found or the input is invalid, an error message is returned.
    """
```'''
    mock_product_db = {'iphone_16': {'name': 'Apple iPhone 16', 'best_price': 1099.0, 'currency': 'USD', 'purchase_channels': [{'vendor': 'Apple Store', 'url': 'https://www.apple.com/iphone-16/', 'price': 1099.0}, {'vendor': 'Best Buy', 'url': 'https://www.bestbuy.com/iphone-16', 'price': 1099.0}, {'vendor': 'Amazon', 'url': 'https://www.amazon.com/dp/B0IPHONE16', 'price': 1079.0}]}, 'mac_air_13': {'name': 'MacBook Air 13-inch M3', 'best_price': 1099.0, 'currency': 'USD', 'purchase_channels': [{'vendor': 'Apple Store', 'url': 'https://www.apple.com/macbook-air-13/', 'price': 1099.0}, {'vendor': 'Best Buy', 'url': 'https://www.bestbuy.com/macbook-air-13', 'price': 1049.0}, {'vendor': 'Amazon', 'url': 'https://www.amazon.com/dp/B0MACBOOKAIR13', 'price': 1029.0}, {'vendor': 'B&H Photo Video', 'url': 'https://www.bhphotovideo.com/macbook-air-13', 'price': 1079.0}]}, 'high_perf_graphics_laptop': {'name': 'Dell XPS 17 (2024) - High Performance', 'best_price': 2499.0, 'currency': 'USD', 'purchase_channels': [{'vendor': 'Dell Official Store', 'url': 'https://www.dell.com/xps-17', 'price': 2499.0}, {'vendor': 'Amazon', 'url': 'https://www.amazon.com/dp/B0XPS17', 'price': 2399.0}, {'vendor': 'B&H Photo Video', 'url': 'https://www.bhphotovideo.com/xps-17', 'price': 2449.0}]}}
    if not isinstance(product_name, str) or not product_name.strip():
        return 'Error: Invalid product identifier. Please provide a non-empty string.'
    normalized_product_name = product_name.strip()
    if ' ' in normalized_product_name:
        return "Error: 'product_name' must use underscores (e.g., 'mac_air_13')."
    normalized_product_name = normalized_product_name.lower()
    if normalized_product_name in mock_product_db:
        product_info = mock_product_db[normalized_product_name]
        best_channel = min(product_info['purchase_channels'], key=lambda x: x['price'])
        return f"Best price for {product_info['name']}: {product_info['currency']} {best_channel['price']:.2f} from {best_channel['vendor']} ({best_channel['url']})."
    else:
        return f"Error: No pricing information found for product ID '{product_name}'."
if __name__ == '__main__':
    mcp.run(transport='stdio')