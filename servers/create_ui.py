from mcp.server.fastmcp import FastMCP
mcp = FastMCP('create_ui')

@mcp.tool()
def create_ui(description: str) -> str:
    '''```python
    """
    Generates web UI components using shadcn/ui components and Tailwind CSS.

    This function creates a web user interface based on the provided description.
    It utilizes shadcn/ui components and Tailwind CSS to build responsive and 
    visually appealing UI elements. Use this function when the description 
    includes references to UI requirements.

    Args:
        description (str): A non-empty string describing the type of UI to create.
            It should contain keywords like 'e-commerce' or 'flight' to select 
            specific UI templates.

    Returns:
        str: A message indicating the successful creation of UI components 
        tailored to the specified description using shadcn/ui and Tailwind CSS.
    """
```'''
    mock_ui_templates = {'ecommerce_frontend': {'description': 'A responsive e-commerce front-end using shadcn/ui components and Tailwind CSS.', 'components': ['ProductCard with image, name, price, and Add to Cart button', 'ProductGrid to display multiple ProductCards', 'SearchBar with real-time filtering', 'ShoppingCartSidebar with item list and checkout button'], 'notes': 'Data binding to product API endpoints, responsive for desktop and mobile.'}, 'flight_display': {'description': 'A flight information display board component using shadcn/ui and Tailwind CSS.', 'components': ['Table with columns: Flight No, Destination, Departure Time, Status', 'StatusBadge component with color coding', 'RefreshButton to reload flight data'], 'notes': 'Real-time updates via WebSocket or polling.'}}
    if not isinstance(description, str) or not description.strip():
        raise ValueError("Invalid input: 'description' must be a non-empty string.")
    desc_lower = description.lower()
    selected_template = None
    if 'e-commerce' in desc_lower or 'ecommerce' in desc_lower:
        selected_template = mock_ui_templates['ecommerce_frontend']
    elif 'flight' in desc_lower:
        selected_template = mock_ui_templates['flight_display']
    if selected_template:
        return f"UI components for '{selected_template['description']}' created successfully using shadcn/ui and Tailwind CSS."
    else:
        return 'UI components created successfully using shadcn/ui and Tailwind CSS.'
if __name__ == '__main__':
    mcp.run(transport='stdio')