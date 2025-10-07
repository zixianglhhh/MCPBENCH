from mcp.server.fastmcp import FastMCP
mcp = FastMCP('user_purchase_history')

@mcp.tool()
def user_purchase_history(customer_ids: list[str], start_date: str, end_date: str) -> str:
    '''```python
    """
    Retrieves the purchase history of specified customers within a given date range.

    This function filters and returns the purchase history for each customer ID provided,
    listing all items purchased within the specified start and end dates.

    Args:
        customer_ids (list[str]): A list of customer IDs as strings for whom the purchase history is to be retrieved.
        start_date (str): The start date of the range in ISO 8601 format (YYYY-MM-DD).
        end_date (str): The end date of the range in ISO 8601 format (YYYY-MM-DD).

    Returns:
        str: A string representation of each customer ID followed by a list of purchased items within the date range.
             Each customer's information is separated by a newline.
    """
```'''
    mock_purchase_db = {'David': [{'purchase_id': 'P1001', 'date': '2024-01-15', 'items': ['Laptop', 'Mouse'], 'total_amount': 1200.5, 'session_id': 'S001'}, {'purchase_id': 'P1002', 'date': '2024-03-10', 'items': ['Headphones'], 'total_amount': 150.0, 'session_id': 'S002'}, {'purchase_id': 'P1003', 'date': '2025-02-05', 'items': ['Keyboard', 'Monitor'], 'total_amount': 450.75, 'session_id': 'S005'}], 'Sam': [{'purchase_id': 'P2001', 'date': '2024-02-21', 'items': ['Smartphone'], 'total_amount': 899.99, 'session_id': 'S003'}, {'purchase_id': 'P2002', 'date': '2024-01-03', 'items': ['Tablet', 'Stylus'], 'total_amount': 650.0, 'session_id': 'S004'}]}
    import datetime
    if not isinstance(customer_ids, list) or not all((isinstance(cid, str) for cid in customer_ids)):
        raise ValueError('customer_ids must be a list of strings.')
    try:
        start_dt = datetime.date.fromisoformat(start_date)
        end_dt = datetime.date.fromisoformat(end_date)
    except ValueError:
        raise ValueError('start_date and end_date must be valid ISO 8601 date strings (YYYY-MM-DD).')
    if start_dt > end_dt:
        raise ValueError('start_date cannot be after end_date.')
    filtered_data = {}
    for cid in customer_ids:
        if cid in mock_purchase_db:
            filtered_purchases = [record for record in mock_purchase_db[cid] if start_dt <= datetime.date.fromisoformat(record['date']) <= end_dt]
            if filtered_purchases:
                filtered_data[cid] = filtered_purchases
    result = {}
    for (cid, purchases) in filtered_data.items():
        all_items = []
        for purchase in purchases:
            all_items.extend(purchase['items'])
        result[cid] = all_items
    output_lines = []
    for (cid, items) in result.items():
        output_lines.append(f'{cid}: {items}')
    return '\n'.join(output_lines)
if __name__ == '__main__':
    mcp.run(transport='stdio')