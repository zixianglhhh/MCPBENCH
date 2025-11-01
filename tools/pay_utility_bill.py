from mcp.server.fastmcp import FastMCP
from typing import Literal
mcp = FastMCP('pay_utility_bill')

@mcp.tool()
def pay_utility_bill(account_number: str, provider: str, amount: float, method: Literal['online', 'in_person', 'auto_debit']='online') -> str:
    '''"""
Submit a payment request for a household utility bill.

Supports electricity, water, gas, and internet service providers stored in the mock
billing registry below. The `amount` must match a pending balance or the payment
will be rejected. This tool simulates a payment gateway and does not perform any
real transactions.

Args:
    account_number (str): Unique account identifier registered with the provider.
    provider (str): Utility provider name, case-insensitive (e.g., "Seattle Water").
    amount (float): Payment amount in USD. Must equal the pending balance on record.
    method (Literal['online', 'in_person', 'auto_debit']): Preferred payment channel.

Returns:
    str: Confirmation string when successful or a descriptive error message.
"""'''
    billing_registry = {
        'Seattle Power': {'A10293': {'balance': 84.71, 'due_date': '11/20/2025'}},
        'Seattle Water': {'W55821': {'balance': 42.18, 'due_date': '11/22/2025'}},
        'Metro Gas': {'G90110': {'balance': 67.44, 'due_date': '11/18/2025'}},
        'Northlink Internet': {'N77654': {'balance': 59.99, 'due_date': '11/25/2025'}},
        'Evergreen Solar': {'E44567': {'balance': 35.12, 'due_date': '11/28/2025'}},
    }
    normalized_provider = provider.strip().title() if provider else ''
    if not account_number:
        return "Error: 'account_number' is required."
    if not normalized_provider:
        return "Error: 'provider' is required."
    if normalized_provider not in billing_registry:
        return f"Error: Provider '{provider}' not recognized."
    provider_accounts = billing_registry[normalized_provider]
    if account_number not in provider_accounts:
        return f"Error: No record found for account '{account_number}'."
    account_record = provider_accounts[account_number]
    pending_balance = account_record['balance']
    if amount != pending_balance:
        return f"Error: Payment amount must match the pending balance of ${pending_balance:.2f}."
    if method not in ['online', 'in_person', 'auto_debit']:
        return "Error: Unsupported payment method."
    confirmation = (
        "Payment submitted successfully!\n"
        f"Provider: {normalized_provider}\n"
        f"Account: {account_number}\n"
        f"Amount: ${amount:.2f}\n"
        f"Due Date: {account_record['due_date']}\n"
        f"Method: {method}"
    )
    return confirmation
if __name__ == '__main__':
    mcp.run(transport='stdio')
