from mcp.server.fastmcp import FastMCP
mcp = FastMCP('make_reservation')

@mcp.tool()
def make_reservation(restaurant_name) -> str:
    '''"""
Attempt to make a reservation at a specified restaurant.

This function simulates the process of creating a reservation for the given
restaurant name and returns a confirmation message.

Args:
    restaurant_name (str): The name of the restaurant where the reservation
        should be made.

Returns:
    str: A success message confirming the reservation at the specified
    restaurant.
"""'''
    return f'Success: Reservation made at {restaurant_name}.'
if __name__ == '__main__':
    mcp.run(transport='stdio')