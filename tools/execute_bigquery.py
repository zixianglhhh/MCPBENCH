from mcp.server.fastmcp import FastMCP
mcp = FastMCP('execute_bigquery')

@mcp.tool()
def execute_bigquery(query: str, project_id: str) -> str:
    '''```python
    """
    Executes a BigQuery SQL query and returns the results as a JSON string.

    This function is designed to execute SQL queries against a BigQuery dataset
    within a specified Google Cloud project. The query must be in the format
    "SELECT * FROM <table_name>", and it retrieves all rows from the specified
    table.

    Args:
        query (str): A non-empty string representing the SQL query to be executed.
                     The query should be in the format "SELECT * FROM <table_name>".
        project_id (str): A non-empty string representing the Google Cloud project ID
                          where the BigQuery dataset is located.

    Returns:
        str: A JSON-formatted string containing the query execution status and the
             retrieved rows. If the query is successful, the JSON includes a "status"
             key with the value "success" and a "rows" key containing the result set.
             If no rows are found, "rows" will be an empty list.
    """
```'''
    if not isinstance(query, str) or not query.strip():
        raise ValueError("Parameter 'query' must be a non-empty string.")
    if not isinstance(project_id, str) or not project_id.strip():
        raise ValueError("Parameter 'project_id' must be a non-empty string.")
    mock_bigquery_db = {'SELECT * FROM business_data_summary': [{'month': '2024-01', 'total_revenue': 125000.5, 'total_expenses': 83000.75, 'net_profit': 42000.75}, {'month': '2024-02', 'total_revenue': 132500.0, 'total_expenses': 85000.0, 'net_profit': 47500.0}, {'month': '2024-03', 'total_revenue': 128750.25, 'total_expenses': 84000.1, 'net_profit': 44750.15}], 'SELECT * FROM pipedrive_sales_pipeline': [{'deal_id': 101, 'stage': 'Proposal', 'value': 15000.0, 'expected_close_date': '2024-04-15'}, {'deal_id': 102, 'stage': 'Negotiation', 'value': 25000.0, 'expected_close_date': '2024-04-20'}, {'deal_id': 103, 'stage': 'Closed Won', 'value': 30000.0, 'expected_close_date': '2024-03-28'}], 'SELECT * FROM zoho_invoice_payments': [{'invoice_id': 'INV-001', 'customer': 'Acme Corp', 'amount_paid': 5000.0, 'payment_date': '2024-03-01'}, {'invoice_id': 'INV-002', 'customer': 'Beta LLC', 'amount_paid': 7500.0, 'payment_date': '2024-03-05'}, {'invoice_id': 'INV-003', 'customer': 'Gamma Inc', 'amount_paid': 6200.0, 'payment_date': '2024-03-07'}], 'SELECT * FROM movie_reviews': [{'movie_id': 1, 'title': 'The Dark Knight', 'rating': 9.0, 'review_text': 'Excellent superhero film with great performances', 'user_id': 'user_001', 'review_date': '2024-01-15'}, {'movie_id': 2, 'title': 'Inception', 'rating': 8.8, 'review_text': 'Mind-bending thriller with amazing visuals', 'user_id': 'user_002', 'review_date': '2024-01-20'}, {'movie_id': 3, 'title': 'Interstellar', 'rating': 8.6, 'review_text': 'Beautiful sci-fi with emotional depth', 'user_id': 'user_003', 'review_date': '2024-02-01'}, {'movie_id': 4, 'title': 'Top Gun: Maverick', 'rating': 8.7, 'review_text': 'Thrilling sequel with incredible action sequences', 'user_id': 'user_004', 'review_date': '2024-02-10'}, {'movie_id': 5, 'title': 'Dune', 'rating': 8.2, 'review_text': 'Epic sci-fi with stunning cinematography', 'user_id': 'user_005', 'review_date': '2024-02-15'}], 'SELECT * FROM us-housing-project': [{'property_id': 'US001', 'address': '123 Main St, San Francisco, CA', 'price': 850000, 'bedrooms': 3, 'bathrooms': 2, 'sqft': 1200, 'year_built': 1995, 'property_type': 'Single Family'}, {'property_id': 'US002', 'address': '456 Oak Ave, Los Angeles, CA', 'price': 650000, 'bedrooms': 2, 'bathrooms': 1, 'sqft': 950, 'year_built': 1988, 'property_type': 'Condo'}, {'property_id': 'US003', 'address': '789 Pine St, Seattle, WA', 'price': 720000, 'bedrooms': 4, 'bathrooms': 3, 'sqft': 1800, 'year_built': 2005, 'property_type': 'Single Family'}, {'property_id': 'US004', 'address': '321 Elm St, Austin, TX', 'price': 480000, 'bedrooms': 3, 'bathrooms': 2, 'sqft': 1400, 'year_built': 2010, 'property_type': 'Townhouse'}, {'property_id': 'US005', 'address': '654 Maple Dr, Denver, CO', 'price': 580000, 'bedrooms': 2, 'bathrooms': 2, 'sqft': 1100, 'year_built': 2000, 'property_type': 'Condo'}]}
    normalized_query = query.strip().rstrip(';')
    if normalized_query in mock_bigquery_db:
        results = mock_bigquery_db[normalized_query]
        import json
        return json.dumps({'status': 'success', 'rows': results}, indent=2)
    else:
        return '{"status": "success", "rows": []}'
if __name__ == '__main__':
    mcp.run(transport='stdio')