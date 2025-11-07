from mcp.server.fastmcp import FastMCP
mcp = FastMCP('pet_vaccination_schedule')

@mcp.tool()
def pet_vaccination_schedule(pet_id: str) -> str:
    '''"""
Return the vaccination status and next due date for a registered pet.

The registry tracks core vaccinations for dogs and cats. The response outlines
completed vaccines, doses remaining, and the upcoming appointment window.

Args:
    pet_id (str): Clinic-issued identifier printed on the pet wellness card.

Returns:
    str: Multi-line status summary or a not-found error.
"""'''
    registry = {
        'DOG-1122': {
            'species': 'Dog',
            'name': 'Bailey',
            'vaccines': {
                'Rabies': {'status': 'Complete', 'next_due': '2026-04-15'},
                'DHPP': {'status': 'Booster due', 'next_due': '2025-11-20'},
            },
        },
        'CAT-7765': {
            'species': 'Cat',
            'name': 'Miso',
            'vaccines': {
                'Rabies': {'status': 'Complete', 'next_due': '2027-01-05'},
                'FVRCP': {'status': 'Scheduled', 'next_due': '2025-11-08'},
            },
        },
        'DOG-8899': {
            'species': 'Dog',
            'name': 'Rocky',
            'vaccines': {
                'Leptospirosis': {'status': 'Overdue', 'next_due': '2025-10-10'},
                'Rabies': {'status': 'Complete', 'next_due': '2026-09-01'},
            },
        },
    }
    if not pet_id:
        return "Error: 'pet_id' is required."
    record = registry.get(pet_id.upper())
    if not record:
        return f"Error: Pet '{pet_id}' not found."
    lines = [f"Name: {record['name']}", f"Species: {record['species']}"]
    for vaccine, details in record['vaccines'].items():
        lines.append(f"- {vaccine}: {details['status']} (Next Due: {details['next_due']})")
    return "\n".join(lines)
if __name__ == '__main__':
    mcp.run(transport='stdio')
