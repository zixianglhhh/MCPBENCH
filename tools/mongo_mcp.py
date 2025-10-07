from mcp.server.fastmcp import FastMCP
mcp = FastMCP('mongo_mcp')

@mcp.tool()
def mongo_mcp(mongoUri: str, collection_name: str) -> str:
    '''```python
    """
    A tool that enables querying of a MongoDB database using natural language via MCP.

    Args:
        mongoUri (str): A non-empty string representing the MongoDB connection URI.
        collection_name (str): A non-empty string specifying the name of the collection to query.

    Returns:
        str: A formatted string containing the retrieved data from the specified collection.
        If the database or collection is not found, an error message is returned.
    """
```'''
    if not isinstance(mongoUri, str) or not mongoUri.strip():
        raise ValueError('Invalid mongoUri: must be a non-empty string representing the MongoDB connection string.')
    if not isinstance(collection_name, str) or not collection_name.strip():
        raise ValueError('Invalid collection_name: must be a non-empty string representing the collection name.')
    customers_collection = [{'name': 'Ocean', 'postal_code': '90210', 'email': 'ocean@example.com', 'phone': '555-1234'}, {'name': 'Alice', 'postal_code': '10001', 'email': 'alice@example.com', 'phone': '555-5678'}, {'name': 'Bob', 'postal_code': '30301', 'email': 'bob@example.com', 'phone': '555-8765'}]
    products_collection = [{'product_name': 'Laptop', 'category': 'Electronics', 'price': 1200.5, 'yearly_sales': [{'year': '2023', 'units_sold': 120, 'revenue': 144060.0}, {'year': '2024', 'units_sold': 180, 'revenue': 216090.0}, {'year': '2025', 'units_sold': 240, 'revenue': 288120.0}]}, {'product_name': 'Mouse', 'category': 'Electronics', 'price': 25.0, 'yearly_sales': [{'year': '2023', 'units_sold': 480, 'revenue': 12000.0}, {'year': '2024', 'units_sold': 600, 'revenue': 15000.0}, {'year': '2025', 'units_sold': 720, 'revenue': 18000.0}]}, {'product_name': 'Headphones', 'category': 'Electronics', 'price': 150.0, 'yearly_sales': [{'year': '2023', 'units_sold': 96, 'revenue': 14400.0}, {'year': '2024', 'units_sold': 144, 'revenue': 21600.0}, {'year': '2025', 'units_sold': 192, 'revenue': 28800.0}]}, {'product_name': 'Smartphone', 'category': 'Electronics', 'price': 899.99, 'yearly_sales': [{'year': '2023', 'units_sold': 60, 'revenue': 53999.4}, {'year': '2024', 'units_sold': 90, 'revenue': 80999.1}, {'year': '2025', 'units_sold': 120, 'revenue': 107998.8}]}, {'product_name': 'Tablet', 'category': 'Electronics', 'price': 600.0, 'yearly_sales': [{'year': '2023', 'units_sold': 36, 'revenue': 21600.0}, {'year': '2024', 'units_sold': 54, 'revenue': 32400.0}, {'year': '2025', 'units_sold': 72, 'revenue': 43200.0}]}, {'product_name': 'Stylus', 'category': 'Accessories', 'price': 50.0, 'yearly_sales': [{'year': '2023', 'units_sold': 120, 'revenue': 6000.0}, {'year': '2024', 'units_sold': 180, 'revenue': 9000.0}, {'year': '2025', 'units_sold': 240, 'revenue': 12000.0}]}]
    mock_databases = {'mongodb://localhost:27017/customers_db': {'customers': customers_collection}, 'mongodb://localhost:27017/product_detail': {'products': products_collection}}
    if mongoUri not in mock_databases:
        return f"Database '{mongoUri}' not found in mock databases."
    if collection_name not in mock_databases[mongoUri]:
        return f"Collection '{collection_name}' not found in database '{mongoUri}'."
    collection_data = mock_databases[mongoUri][collection_name]
    if collection_name == 'customers':
        customer_list = []
        for customer in collection_data:
            customer_list.append(f"Name: {customer['name']}, Postal Code: {customer['postal_code']}, Email: {customer['email']}, Phone: {customer['phone']}")
        return f"Retrieved {len(collection_data)} customers from '{collection_name}' collection:\n" + '\n'.join(customer_list)
    elif collection_name == 'products':
        product_list = []
        for product in collection_data:
            product_info = f"Product: {product['product_name']} ({product['category']}) - Price: ${product['price']}"
            yearly_info = []
            for year_data in product['yearly_sales']:
                yearly_info.append(f"{year_data['year']}: {year_data['units_sold']} units, ${year_data['revenue']}")
            product_info += f"\n  Sales: {', '.join(yearly_info)}"
            product_list.append(product_info)
        return f"Retrieved {len(collection_data)} products from '{collection_name}' collection:\n" + '\n'.join(product_list)
    else:
        return f"Retrieved {len(collection_data)} documents from '{collection_name}' collection in database '{mongoUri}'."
if __name__ == '__main__':
    mcp.run(transport='stdio')