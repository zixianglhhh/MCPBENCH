from mcp.server.fastmcp import FastMCP
mcp = FastMCP('Execute_Database_Query')

@mcp.tool()
def Execute_Database_Query(database: str, query: str, parameters: str) -> str:
    '''```python
    """
    Execute a SQL query within a specified database.

    Args:
        database (str): The name of the database where the query will be executed.
        query (str): The SQL query string to be executed. Supports SELECT statements.
        parameters (dict): A dictionary of parameters for the WHERE clause in the query.

    Returns:
        str: A message indicating the success of the query execution and the number of rows returned,
             or an error message if the execution fails due to invalid inputs or database/table not found.
    """
```'''
    if not database or not isinstance(database, str):
        return "Error: 'database' parameter must be a non-empty string."
    if not query or not isinstance(query, str):
        return "Error: 'query' parameter must be a non-empty string."
    if not parameters or not isinstance(parameters, dict):
        return "Error: 'parameters' parameter must be a non-empty dictionary."
    mock_databases = {'AdventureWorks': {'Person.Person': [{'BusinessEntityID': 1, 'FirstName': 'Ken', 'LastName': 'Sánchez'}, {'BusinessEntityID': 2, 'FirstName': 'Terri', 'LastName': 'Duffy'}, {'BusinessEntityID': 3, 'FirstName': 'Roberto', 'LastName': 'Tamburello'}, {'BusinessEntityID': 4, 'FirstName': 'Rob', 'LastName': 'Walters'}, {'BusinessEntityID': 5, 'FirstName': 'Gail', 'LastName': 'Erickson'}, {'BusinessEntityID': 6, 'FirstName': 'Jossef', 'LastName': 'Goldberg'}, {'BusinessEntityID': 7, 'FirstName': 'Dylan', 'LastName': 'Miller'}, {'BusinessEntityID': 8, 'FirstName': 'Diane', 'LastName': 'Margheim'}, {'BusinessEntityID': 9, 'FirstName': 'Gigi', 'LastName': 'Matthew'}, {'BusinessEntityID': 10, 'FirstName': 'Michael', 'LastName': 'Raheem'}], 'Sales.SalesOrderHeader': [{'SalesOrderID': 43659, 'OrderDate': '2024-05-01', 'TotalDue': 4721.52}, {'SalesOrderID': 43660, 'OrderDate': '2024-05-03', 'TotalDue': 1543.22}]}}
    if database not in mock_databases:
        return f"Error: Database '{database}' not found."
    db_data = mock_databases[database]
    query_upper = query.strip().upper()
    if query_upper.startswith('SELECT'):
        table_name = None
        for tbl in db_data.keys():
            if tbl.upper() in query_upper:
                table_name = tbl
                break
        if not table_name:
            return 'Error: Table not found in mock database.'
        results = db_data[table_name]
        if 'TOP' in query_upper:
            try:
                top_n = int(query_upper.split('TOP')[1].split()[0])
                results = results[:top_n]
            except Exception:
                pass
        if 'WHERE' in query_upper and parameters:
            filtered_results = []
            where_part = query_upper.split('WHERE')[1]
            for row in results:
                match = True
                for (key, value) in parameters.items():
                    if key.upper() in where_part and str(row.get(key, '')).upper() != str(value).upper():
                        match = False
                        break
                if match:
                    filtered_results.append(row)
            results = filtered_results
        return f'Query executed successfully. Rows returned: {results}'
    else:
        return f"Query executed successfully in database '{database}'. No result set returned."
if __name__ == '__main__':
    mcp.run(transport='stdio')