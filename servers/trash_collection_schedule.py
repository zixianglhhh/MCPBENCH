from mcp.server.fastmcp import FastMCP
mcp = FastMCP('trash_collection_schedule')

@mcp.tool()
def trash_collection_schedule(service_address: str, waste_type: str) -> str:
    '''"""
Retrieve the curbside pickup schedule for a specific waste stream.

Supported waste streams are `garbage`, `recycling`, and `compost`. Addresses are
indexed by route code in the mock database. The tool returns the next pickup day
and any holiday adjustments.

Args:
    service_address (str): Street address registered with the sanitation service.
    waste_type (str): Waste category to look up. One of `garbage`, `recycling`, `compost`.

Returns:
    str: Upcoming pickup window or an error message when the address is unknown.
"""'''
    routes = {
        '742 Evergreen Terrace': {
            'garbage': {'next_pickup': '11/04/2025', 'note': 'Set out by 7:00 AM'},
            'recycling': {'next_pickup': '11/07/2025', 'note': 'Blue bin only'},
            'compost': {'next_pickup': '11/04/2025', 'note': 'Holiday schedule - pickup delayed one day'},
        },
        '1234 Lakeview Drive': {
            'garbage': {'next_pickup': '11/02/2025', 'note': 'Normal service'},
            'recycling': {'next_pickup': '11/09/2025', 'note': 'Rinse containers'},
            'compost': {'next_pickup': '11/02/2025', 'note': 'Place cart 3 ft from bins'},
        },
        '501 Pine Street': {
            'garbage': {'next_pickup': '11/03/2025', 'note': 'Extra bag tags required'},
            'recycling': {'next_pickup': '11/10/2025', 'note': 'Flatten cardboard'},
            'compost': {'next_pickup': '11/03/2025', 'note': 'Remove produce stickers'},
        },
    }
    if not service_address:
        return "Error: 'service_address' is required."
    if waste_type not in ['garbage', 'recycling', 'compost']:
        return "Error: Unsupported waste type."
    record = routes.get(service_address)
    if not record:
        return f"Error: Address '{service_address}' not found."
    schedule = record[waste_type]
    return (
        f"Next Pickup: {schedule['next_pickup']}\n"
        f"Instructions: {schedule['note']}"
    )
if __name__ == '__main__':
    mcp.run(transport='stdio')
