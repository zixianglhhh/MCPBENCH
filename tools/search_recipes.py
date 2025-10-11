from mcp.server.fastmcp import FastMCP
mcp = FastMCP('search_recipes')

@mcp.tool()
def search_recipes(name: str) -> str:
    '''```python
"""
Search and retrieve cooking or drink recipes from an online recipe catalog or database.

This function allows users to search for recipes by specifying a search term in the format
"xxx recipes", where "xxx" represents the type of recipes desired (e.g., "halal", "cocktail").
The search is case-insensitive and matches recipes based on their title containing the search term.

Args:
    name (str): A non-empty string specifying the type of recipes to search for, formatted as
                "xxx recipes". Examples include "halal recipes", "cocktail recipes", and 
                "mocktail recipes".

Returns:
    str: A formatted string containing the details of matching recipes, including title, 
         ingredients, instructions, and timing information. If no recipes are found, an error 
         message is returned indicating that no matches were found for the specified search term.

Example:
    search_recipes("halal recipes")  # Returns halal cooking recipes
    search_recipes("cocktail recipes")  # Returns alcoholic drink recipes

Note:
    The search term must end with "recipes" and is case-insensitive.
"""
```'''
    if not isinstance(name, str) or not name.strip():
        return "Error: 'name' must be a non-empty string."
    mock_recipes_db = [{'title': 'Halal Chicken Biryani', 'ingredients': ['Basmati rice', 'Halal chicken', 'Onions', 'Tomatoes', 'Yogurt', 'Ginger-garlic paste', 'Spices', 'Fresh coriander'], 'instructions': 'Marinate chicken with yogurt and spices, cook with onions and tomatoes, layer with partially cooked rice, steam until done.', 'prep_time': '20 minutes', 'cook_time': '40 minutes', 'tags': ['halal', 'rice', 'main course', 'South Asian']}, {'title': 'Halal Beef Shawarma', 'ingredients': ['Halal beef', 'Pita bread', 'Garlic sauce', 'Lettuce', 'Tomatoes', 'Cucumber', 'Spices'], 'instructions': 'Marinate beef with spices, grill until tender, serve in pita bread with vegetables and garlic sauce.', 'prep_time': '15 minutes', 'cook_time': '20 minutes', 'tags': ['halal', 'Middle Eastern', 'wrap', 'street food']}, {'title': 'Classic Mojito (Non-Alcoholic)', 'ingredients': ['Fresh mint leaves', 'Lime juice', 'Sugar', 'Soda water', 'Ice'], 'instructions': 'Muddle mint leaves with sugar and lime juice, add ice, top with soda water, stir gently.', 'prep_time': '5 minutes', 'cook_time': '0 minutes', 'tags': ['mocktail', 'drink', 'refreshing', 'cocktail']}, {'title': 'Margarita Cocktail', 'ingredients': ['Tequila', 'Triple sec', 'Lime juice', 'Salt', 'Ice'], 'instructions': 'Shake tequila, triple sec, and lime juice with ice, strain into glass with salted rim.', 'prep_time': '5 minutes', 'cook_time': '0 minutes', 'tags': ['cocktail', 'drink', 'competition']}, {'title': 'Toronto Maple Leafs Blue Lagoon Cocktail', 'ingredients': ['Vodka', 'Blue curaçao', 'Lemonade', 'Ice', 'Lemon slice'], 'instructions': "Mix vodka, blue curaçao, and lemonade over ice, garnish with lemon slice. Inspired by the Toronto Maple Leafs' blue colors.", 'prep_time': '5 minutes', 'cook_time': '0 minutes', 'tags': ['cocktail', 'drink', 'themed', 'Toronto Maple Leafs', 'competition']}]
    search_term = name.strip().lower()
    if search_term.endswith('recipes'):
        base_term = search_term[:-7].strip()
    elif search_term.endswith('recipe'):
        base_term = search_term[:-6].strip()
    else:
        base_term = search_term
    if not base_term:
        return "Error: Invalid format. Please use format like 'halal recipes' or 'cocktail recipes'."
    matching_recipes = []
    for recipe in mock_recipes_db:
        # Check if search term appears in the recipe title (case-insensitive)
        if base_term in recipe['title'].lower():
            matching_recipes.append(recipe)
    if not matching_recipes:
        return f"No recipes found with '{base_term}' in the title. Please try a different search."
    output_lines = []
    for r in matching_recipes:
        output_lines.append(f"Name: {r['title']}")
        output_lines.append(f"Ingredients: {', '.join(r['ingredients'])}")
        output_lines.append(f"Instruction: {r['instructions']}")
        output_lines.append(f"Prep Time: {r['prep_time']}")
        output_lines.append(f"Cook Time: {r['cook_time']}")
        output_lines.append('-' * 50)
    return '\n'.join(output_lines)
if __name__ == '__main__':
    mcp.run(transport='stdio')