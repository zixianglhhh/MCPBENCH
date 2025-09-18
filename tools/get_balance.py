from mcp.server.fastmcp import FastMCP
mcp = FastMCP('get_balance')

@mcp.tool()
def get_balance(account_type) -> str:
    '''"""
Check the balance for a specified account type.

The account type must be either "checking" or "savings". This function returns 
a formatted string indicating the current balance for the selected account.

Args:
    account_type (str): The type of account to check. Must be either 
        "checking" or "savings".

Returns:
    str: A message stating the balance of the specified account in USD.
"""'''
    mock_balance = {'checking': 1500, 'savings': 3000}
    return f"The balance of the user's {account_type} account is {mock_balance[account_type]} USD."
if __name__ == '__main__':
    mcp.run(transport='stdio')