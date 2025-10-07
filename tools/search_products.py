from mcp.server.fastmcp import FastMCP
mcp = FastMCP('search_products')

@mcp.tool()
def search_products(brand: str, max_results: str) -> str:
    '''```python
    """
    Searches for products by brand name and returns a formatted list of matching products.

    Args:
        brand (str): The brand name to search for products. Must be a non-empty string.
        max_results (str): The maximum number of results to return, specified as a positive integer in string format.

    Returns:
        str: A formatted string listing the products that match the brand search criteria. If no products are found, 
        returns a message indicating no matches. If input validation fails, returns an error message.
    """
```'''
    mock_products_db = [{'id': 'B001', 'name': 'Salalad Organic Mixed Salad Pack', 'brand': 'Salalad', 'category': 'Food', 'description': 'A fresh organic salad mix containing lettuce, spinach, and arugula.', 'price': '$4.99'}, {'id': 'B002', 'name': 'Salalad Caesar Salad Kit', 'brand': 'Salalad', 'category': 'Food', 'description': 'A ready-to-eat Caesar salad with dressing and croutons.', 'price': '$5.49'}, {'id': 'B003', 'name': 'Salalad Greek Salad Bowl', 'brand': 'Salalad', 'category': 'Food', 'description': 'A Greek-style salad with feta cheese, olives, and cucumbers.', 'price': '$6.25'}, {'id': 'B004', 'name': 'Salalad Asian Slaw Mix', 'brand': 'Salalad', 'category': 'Food', 'description': 'A crunchy Asian-inspired slaw with cabbage, carrots, and sesame dressing.', 'price': '$5.99'}, {'id': 'B005', 'name': 'Salalad Mediterranean Bowl', 'brand': 'Salalad', 'category': 'Food', 'description': 'A Mediterranean-style salad with tomatoes, olives, and feta cheese.', 'price': '$6.75'}]
    if not isinstance(brand, str) or not brand.strip():
        return "Error: 'brand' must be a non-empty string."
    if not isinstance(max_results, str) or not max_results.isdigit() or int(max_results) <= 0:
        return "Error: 'max_results' must be a positive integer in string format."
    max_results_int = int(max_results)
    filtered_results = [product for product in mock_products_db if brand.lower() in product['brand'].lower()]
    limited_results = filtered_results[:max_results_int]
    if not limited_results:
        return f"No products found for brand '{brand}'."
    result_str_lines = ['Search Results:']
    for product in limited_results:
        result_str_lines.append(f"- {product['name']} ({product['price']}): {product['description']}")
    return '\n'.join(result_str_lines)
if __name__ == '__main__':
    mcp.run(transport='stdio')