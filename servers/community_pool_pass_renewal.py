from mcp.server.fastmcp import FastMCP
mcp = FastMCP('community_pool_pass_renewal')

@mcp.tool()
def community_pool_pass_renewal(member_id: str, renewal_term: int) -> str:
    '''"""
Process a renewal for a community pool membership pass.

Memberships may be extended in 3, 6, or 12 month increments. The tool validates
member status, calculates the new expiration date, and reports the renewal fee.

Args:
    member_id (str): Unique pass identifier.
    renewal_term (int): Number of months to renew (3, 6, or 12).

Returns:
    str: Renewal confirmation with new expiration date and amount due.
"""'''
    members = {
        'PASS-3301': {'name': 'Jordan Lee', 'expiration': '2025-12-15', 'status': 'Active'},
        'PASS-4488': {'name': 'Priya Patel', 'expiration': '2025-11-20', 'status': 'Active'},
        'PASS-9921': {'name': 'Alex Gomez', 'expiration': '2025-10-01', 'status': 'Expired'},
    }
    pricing = {3: 45.00, 6: 80.00, 12: 150.00}
    if not member_id:
        return "Error: 'member_id' is required."
    if renewal_term not in pricing:
        return "Error: Renewal term must be 3, 6, or 12 months."
    record = members.get(member_id.upper())
    if not record:
        return f"Error: Member '{member_id}' not found."
    if record['status'] == 'Expired' and renewal_term < 6:
        return "Error: Expired memberships require at least a 6-month renewal."
    return (
        f"Renewal successful!\n"
        f"Member: {record['name']}\n"
        f"Current Expiration: {record['expiration']}\n"
        f"New Term: {renewal_term} month(s)\n"
        f"Amount Due: ${pricing[renewal_term]:.2f}"
    )
if __name__ == '__main__':
    mcp.run(transport='stdio')
