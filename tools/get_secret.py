from mcp.server.fastmcp import FastMCP
mcp = FastMCP('get_secret')

@mcp.tool()
def get_secret(secret_name: str, mask_sensitive: bool, confirm_unmask: str) -> str:
    '''```python
    """
    Retrieves a specific secret with options to mask or unmask sensitive fields.

    By default, sensitive fields such as passwords and usernames are masked. 
    To unmask these fields, a confirmation is required.

    Args:
        secret_name (str): The name of the secret to retrieve. If None, a list of available secrets is returned.
        mask_sensitive (bool): If True, masks sensitive fields in the secret data.
        confirm_unmask (str): A confirmation string required to unmask sensitive fields. 
            Must be 'yes, I understand' to proceed with unmasking.

    Returns:
        str: A message indicating the result of the retrieval. This includes the secret data with masked or unmasked 
        sensitive fields, or an error message if the operation fails.
    """
```'''
    mock_secrets_db = {'rds_sqlserver_credentials': {'username': 'app_user', 'password': 'P@ssw0rd!2024', 'host': 'rds-sqlserver-instance.abc123xyz.us-east-1.rds.amazonaws.com', 'port': 1433, 'database': 'production_db'}, 'pyodbc_connection_string': {'connection_string': 'DRIVER={ODBC Driver 18 for SQL Server};SERVER=rds-sqlserver-instance.abc123xyz.us-east-1.rds.amazonaws.com,1433;DATABASE=production_db;UID=app_user;PWD=P@ssw0rd!2024;Encrypt=yes;TrustServerCertificate=no;Connection Timeout=30;'}}
    if secret_name is not None and (not isinstance(secret_name, str)):
        return "Error: 'secret_name' must be a string if provided."
    if not isinstance(mask_sensitive, bool):
        return "Error: 'mask_sensitive' must be a boolean."
    if not isinstance(confirm_unmask, str):
        return "Error: 'confirm_unmask' must be a string."
    if secret_name is None:
        return f"Available secrets: {', '.join(mock_secrets_db.keys())}"
    if secret_name not in mock_secrets_db:
        return f"Error: Secret '{secret_name}' not found."
    secret_data = mock_secrets_db[secret_name].copy()

    def mask_value(value):
        if isinstance(value, str):
            if len(value) <= 4:
                return '*' * len(value)
            return value[0:2] + '*' * (len(value) - 4) + value[-2:]
        return value
    if mask_sensitive:
        for key in secret_data:
            if any((sens in key.lower() for sens in ['password', 'pwd', 'username', 'connection_string'])):
                secret_data[key] = mask_value(secret_data[key])
    elif confirm_unmask.strip().lower() != 'yes, i understand':
        return "Error: Unmasking sensitive data requires confirmation. Please provide 'yes, I understand' as confirm_unmask."
    return f"Retrieved secret '{secret_name}': {secret_data}"
if __name__ == '__main__':
    mcp.run(transport='stdio')