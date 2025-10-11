from mcp.server.fastmcp import FastMCP
mcp = FastMCP('send_transaction')

@mcp.tool()
def send_transaction(target, amount) -> str:
    '''"""
Send a transaction to a specified target with a specified amount.

Args:
    target (str): The recipient of the transaction, such as a username, account ID, or email address.
    amount (float): The amount of money to send, in USD.

Returns:
    str: A confirmation message indicating that the transaction was successful.
"""'''
    return f'Transaction successful! The {target} received {amount} USD.'
if __name__ == '__main__':
    mcp.run(transport='stdio')