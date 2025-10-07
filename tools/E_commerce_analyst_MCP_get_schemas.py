from mcp.server.fastmcp import FastMCP
from typing import List
mcp = FastMCP('E_commerce_analyst_MCP_get_schemas')

@mcp.tool()
def E_commerce_analyst_MCP_get_schemas(database_name: str, schema_filter: List[str]) -> str:
    '''```python
    """
    Retrieves and filters schemas from a specified e-commerce database.

    This function accesses schemas within a given database and filters them
    based on the provided schema names. It returns a formatted string
    describing the schemas and their respective tables.

    Args:
        database_name (str): The name of the database from which to retrieve schemas.
                             If None, the default database is used.
        schema_filter (List[str]): A list of schema names to filter the results.
                                   If empty, all schemas are returned.

    Returns:
        str: A formatted string listing the database name, schemas, and their tables.
             If no schemas match the filter, a message indicating no matches is returned.

    Raises:
        ValueError: If the specified database is not found.
        TypeError: If 'schema_filter' is not a list of strings.
    """
```'''
    mock_databases = {
        'default_ecommerce_db': {
            'products': {'tables': ['product_list', 'product_categories', 'product_reviews'], 
            'description': 'Contains product-related data including details, categories, and reviews.'}, 
            'sales': {'tables': ['sales_orders', 'sales_transactions', 'sales_returns'], 
            'description': 'Contains sales order records, transaction history, and return information.'},
            'customers': {'tables': ['customer_profiles', 'customer_feedback', 'customer_loyalty'], 
            'description': 'Contains customer personal information, feedback, and loyalty program data.'}, 
            'inventory': {'tables': ['stock_levels', 'warehouse_locations', 'supplier_info'], 
            'description': 'Contains inventory stock levels, warehouse data, and supplier details.'}
        },
        'seasonal_sales_db': {
            'promotions': {'tables': ['promo_codes', 'discount_campaigns'], 
            'description': 'Contains promotional codes and discount campaign data for seasonal sales.'}
        }
    }
    if database_name is None:
        db_to_use = 'default_ecommerce_db'
    elif isinstance(database_name, str) and database_name in mock_databases:
        db_to_use = database_name
    else:
        raise ValueError(f"Database '{database_name}' not found in mock databases.")
    if not isinstance(schema_filter, list) or not all((isinstance(s, str) for s in schema_filter)):
        raise TypeError("Parameter 'schema_filter' must be a list of strings.")
    db_schemas = mock_databases[db_to_use]
    if schema_filter:
        filtered_schemas = {schema: info for (schema, info) in db_schemas.items() if schema in schema_filter}
    else:
        filtered_schemas = db_schemas
    if not filtered_schemas:
        return f"No schemas found matching filter {schema_filter} in database '{db_to_use}'."
    output_lines = [f'Database: {db_to_use}', 'Schemas:']
    for (schema_name, schema_info) in filtered_schemas.items():
        output_lines.append(f"  - {schema_name}: {schema_info['description']}")
        output_lines.append(f"    Tables: {', '.join(schema_info['tables'])}")
    return '\n'.join(output_lines)
if __name__ == '__main__':
    mcp.run(transport='stdio')