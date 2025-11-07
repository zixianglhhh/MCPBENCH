from mcp.server.fastmcp import FastMCP

mcp = FastMCP("findParks")

@mcp.tool()
def findParks(stateCode: str, park_type: str, limit: str, activities: str) -> str:
    '''```python
    """
    Search national parks by multiple criteria with simple pagination over mock data.

    This tool demonstrates filtering by state codes, keyword search across name/description, activity filters, and
    paginated output. All data is sourced from an in-memory example dataset for illustrative purposes.

    Args:
        stateCode (str): Comma-separated state codes (e.g., "CA,AZ").
        park_type (str): What type of park you want to find, should all be in lowercase, in the form of xxx park.
        limit (str): How many park per state you want to find in total, in the range [1, 50].
        activities (str): What activities you want to find in the park, should all be in lowercase.

    Returns:
        str: A formatted list of matching parks or an error/empty-result message when no matches or invalid
        parameters are provided.
    """
    ```'''
    # Mock database of national parks
    parks_db = [
        {
            "name": "Yosemite National Park",
            "stateCode": "CA",
            "description": "Known for its waterfalls, deep valleys, grand meadows, and ancient giant sequoias.",
            "activities": ["hiking", "camping", "climbing"],
        },
        {
            "name": "Olympic National Park",
            "stateCode": "WA",
            "description": "Features diverse ecosystems from mountainous areas to rainforests and the Pacific coastline.",
            "activities": ["hiking", "camping", "wildlife watching"],
        },
        {
            "name": "Grand Canyon National Park",
            "stateCode": "AZ",
            "description": "Famous for its immense size and its intricate and colorful landscape.",
            "activities": ["hiking", "rafting"],
        },
        {
            "name": "Yellowstone National Park",
            "stateCode": "WY",
            "description": "Home to a large variety of wildlife and geothermal features like Old Faithful geyser.",
            "activities": ["hiking", "camping", "wildlife watching"],
        },
        {
            "name": "Zion National Park",
            "stateCode": "UT",
            "description": "Known for Zion Canyon's steep red cliffs and scenic views.",
            "activities": ["hiking", "camping", "climbing"],
        },
    ]

    # Validate and process input parameters
    if not stateCode or not park_type or not limit or not activities:
        return "Error: All parameters are required and must not be empty."

    try:
        limit = int(limit)
    except ValueError:
        return "Error: 'limit' must be an integer."

    if limit < 1 or limit > 50:
        return "Error: 'limit' must be between 1 and 50."

    # Parse the input parameters
    state_codes = stateCode.split(",")
    search_activities = activities.split(",")

    # Filter parks based on the criteria
    filtered_parks = [
        park for park in parks_db
        if park['stateCode'] in state_codes and
        park_type.lower() in park['type'].lower() and
           any(activity in search_activities for activity in park['activities'])
    ]

    # Format the output
    if not filtered_parks:
        return "No parks found matching the criteria."

    result = "Matching National Parks:\n"
    for park in filtered_parks:
        result += f"- {park['name']} (State: {park['stateCode']})\n  Description: {park['description']}\n  Activities: {', '.join(park['activities'])}\n\n"

    return result.strip()

if __name__ == "__main__":
    mcp.run(transport='stdio')
