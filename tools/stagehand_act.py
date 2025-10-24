from mcp.server.fastmcp import FastMCP
mcp = FastMCP('stagehand_act')

@mcp.tool()
def stagehand_act(action: str, variables: dict) -> str:
    '''```python
    """
    Performs a specific atomic action on a web page element.

    This function executes actions such as clicking a button or typing text into 
    an input field. It is designed to handle single-step actions only, ensuring 
    that each action is as specific and granular as possible. Examples of valid 
    actions include 'Click the sign in button' or 'Type 'hello' into the search 
    input'. Multi-step actions like 'Order me pizza' or 'Send an email to Paul 
    asking him to call me' should be avoided.

    Args:
        action (str): The action to perform on the web page element. This should 
            be a single-step command, such as 'click' or 'type'.
        variables (dict): A dictionary containing additional parameters required 
            for the action. Must include 'element' to specify the target element 
            and may include 'text' for typing actions or 'selection' for list 
            selection actions.

    Returns:
        str: A message indicating the result of the action performed, such as 
        confirmation of a successful click or type action, or an error message 
        if the action could not be completed.
    """
```'''
    mock_page_elements = {'search_button': {'type': 'button', 'label': 'Search', 'state': 'enabled'}, 'location_permission_popup': {'type': 'popup', 'label': 'Allow location access', 'state': 'visible'}, 'search_input': {'type': 'input', 'label': 'Enter restaurant name or cuisine', 'value': ''}, 'filter_button': {'type': 'button', 'label': 'Filters', 'state': 'enabled'}, 'restaurant_list': {'type': 'list', 'items': []}}
    if not isinstance(action, str):
        raise ValueError("Parameter 'action' must be a string.")
    if not isinstance(variables, dict):
        raise ValueError("Parameter 'variables' must be an object (dict).")
    target_element = variables.get('element')
    if not target_element or target_element not in mock_page_elements:
        raise ValueError(f"Target element '{target_element}' not found in mock page elements.")
    element = mock_page_elements[target_element]
    action_lower = action.lower()
    if 'click' in action_lower:
        if element['type'] == 'button' and element['state'] == 'enabled':
            return f"Clicked the '{element['label']}' button successfully."
        elif element['type'] == 'popup' and element['state'] == 'visible':
            return f"Clicked '{element['label']}' and dismissed the popup."
        else:
            return f"Cannot click on '{element['label']}' because it is not clickable or not enabled."
    elif 'type' in action_lower or 'enter' in action_lower:
        text_to_type = variables.get('text')
        if element['type'] == 'input':
            if not isinstance(text_to_type, str) or not text_to_type.strip():
                raise ValueError("You must provide a non-empty 'text' string to type into the input.")
            element['value'] = text_to_type
            return f"Typed '{text_to_type}' into the '{element['label']}' input field."
        else:
            return f"Cannot type into '{element['label']}' because it is not an input field."
    elif 'select' in action_lower:
        if element['type'] == 'list' and element['items']:
            selection = variables.get('selection')
            if selection in element['items']:
                return f"Selected '{selection}' from the restaurant list."
            else:
                return f"'{selection}' is not available in the restaurant list."
        else:
            return f"No items available to select in '{element['label']}'."
    else:
        return f"Action '{action}' is not supported for element '{element['label']}'."
if __name__ == '__main__':
    mcp.run(transport='stdio')