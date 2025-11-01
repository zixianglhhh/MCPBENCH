from mcp.server.fastmcp import FastMCP
mcp = FastMCP('school_lunch_menu_lookup')

@mcp.tool()
def school_lunch_menu_lookup(school_code: str, menu_date: str) -> str:
    '''"""
Fetch the cafeteria lunch menu for a given school and date.

Menus include entree, side, and vegetarian alternatives. Dates must follow the
`YYYY-MM-DD` format. Only schools in the lookup table below are supported.

Args:
    school_code (str): District-issued school identifier (e.g., "LMS").
    menu_date (str): Desired menu date in `YYYY-MM-DD` format.

Returns:
    str: Formatted menu details or an informative error.
"""'''
    menus = {
        'LMS': {
            '2025-11-03': {
                'entree': 'Chicken Teriyaki Bowl',
                'side': 'Steamed Broccoli',
                'vegetarian': 'Tofu Stir Fry'
            },
            '2025-11-04': {
                'entree': 'Beef Tacos',
                'side': 'Spanish Rice',
                'vegetarian': 'Black Bean Tacos'
            },
        },
        'NHE': {
            '2025-11-03': {
                'entree': 'Baked Ziti',
                'side': 'Garlic Bread',
                'vegetarian': 'Veggie Ziti'
            },
            '2025-11-05': {
                'entree': 'BBQ Chicken Sandwich',
                'side': 'Coleslaw',
                'vegetarian': 'BBQ Jackfruit Sandwich'
            },
        },
        'WVE': {
            '2025-11-04': {
                'entree': 'Turkey Chili',
                'side': 'Cornbread',
                'vegetarian': 'Three-Bean Chili'
            }
        },
    }
    if not school_code:
        return "Error: 'school_code' is required."
    if not menu_date:
        return "Error: 'menu_date' is required."
    school = menus.get(school_code.upper())
    if not school:
        return f"Error: School '{school_code}' is not supported."
    menu = school.get(menu_date)
    if not menu:
        return f"No menu posted for {menu_date}."
    return (
        f"Entree: {menu['entree']}\n"
        f"Side: {menu['side']}\n"
        f"Vegetarian Option: {menu['vegetarian']}"
    )
if __name__ == '__main__':
    mcp.run(transport='stdio')
