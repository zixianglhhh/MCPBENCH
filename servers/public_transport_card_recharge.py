from mcp.server.fastmcp import FastMCP
mcp = FastMCP('public_transport_card_recharge')

@mcp.tool()
def public_transport_card_recharge(card_number: str, amount: float) -> str:
    '''"""
Apply a stored-value recharge to a public transit card.

Cards have maximum balances; recharges must keep the balance under $200. The tool
validates the amount and the card status before confirming the transaction.

Args:
    card_number (str): Transit authority card identifier.
    amount (float): Amount in USD to add. Must be between 5 and 100 inclusive, accurate to one decimal place.

Returns:
    str: Updated balance confirmation or an error message when validation fails.
"""'''
    cards = {
        'ORCA-551122': {'status': 'Active', 'balance': 42.75},
        'ORCA-773344': {'status': 'Active', 'balance': 180.00},
        'ORCA-889910': {'status': 'Suspended', 'balance': 15.25},
    }
    if not card_number:
        return "Error: 'card_number' is required."
    if amount <= 0:
        return "Error: Recharge amount must be positive."
    if amount < 5 or amount > 100:
        return "Error: Amount must be between $5 and $100."
    card = cards.get(card_number.upper())
    if not card:
        return f"Error: Card '{card_number}' not found."
    if card['status'] != 'Active':
        return f"Error: Card status is {card['status']}."
    new_balance = card['balance'] + amount
    if new_balance > 200:
        return "Error: Recharge would exceed maximum balance of $200."
    return (
        f"Recharge successful!\n"
        f"Card: {card_number}\n"
        f"Amount Added: ${amount:.2f}\n"
        f"New Balance: ${new_balance:.2f}"
    )
if __name__ == '__main__':
    mcp.run(transport='stdio')
