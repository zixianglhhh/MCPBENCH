from mcp.server.fastmcp import FastMCP
from typing import List
mcp = FastMCP('grocery_pickup_slots')

@mcp.tool()
def grocery_pickup_slots(store_code: str, pickup_date: str) -> str:
    '''"""
List available curbside pickup slots for a grocery store on a given date.

Stores maintain separate slot inventories. Slots are expressed as 1-hour windows.
The tool will only return openings that still have capacity remaining.

Args:
    store_code (str): Identifier for the grocery location (e.g., "SEA01").
    pickup_date (str): Requested pickup date in `YYYY-MM-DD` format.

Returns:
    str: A newline separated list of open slots or an error when none are free.
"""'''
    slot_inventory = {
        'SEA01': {
            '2025-11-01': {'09:00-10:00': 0, '11:00-12:00': 2, '16:00-17:00': 1},
            '2025-11-02': {'08:00-09:00': 3, '10:00-11:00': 2, '18:00-19:00': 0},
        },
        'BEL02': {
            '2025-11-01': {'12:00-13:00': 1, '14:00-15:00': 1, '19:00-20:00': 1},
            '2025-11-03': {'09:00-10:00': 2, '13:00-14:00': 0, '17:00-18:00': 2},
        },
        'KIR03': {
            '2025-11-02': {'11:00-12:00': 1, '15:00-16:00': 1},
            '2025-11-04': {'10:00-11:00': 2, '16:00-17:00': 2},
        },
    }
    if not store_code:
        return "Error: 'store_code' is required."
    if not pickup_date:
        return "Error: 'pickup_date' is required."
    store = slot_inventory.get(store_code.upper())
    if not store:
        return f"Error: Store '{store_code}' not found."
    day_slots = store.get(pickup_date)
    if not day_slots:
        return f"No pickup slots found for {pickup_date}."
    available = [window for window, capacity in day_slots.items() if capacity > 0]
    if not available:
        return f"All pickup slots are full on {pickup_date}."
    return "Available slots:\n" + "\n".join(available)
if __name__ == '__main__':
    mcp.run(transport='stdio')
