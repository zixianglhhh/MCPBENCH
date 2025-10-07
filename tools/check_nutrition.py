from mcp.server.fastmcp import FastMCP
from typing import List
mcp = FastMCP('check_nutrition')

@mcp.tool()
def check_nutrition(ingredient_list: List[str]) -> str:
    '''```python
"""
Checks the availability of specified ingredients and returns their detailed nutritional information.

This function verifies the presence of each ingredient in a case-insensitive manner against a nutritional database.
It filters out duplicate entries and provides a formatted string containing nutritional details for each available ingredient.

Args:
    ingredient_list (List[str]): A list of ingredients to check for availability. Each ingredient must be a string
                                 and is checked case-insensitively. Duplicate entries are automatically removed.

Returns:
    str: A formatted string listing available ingredients along with their nutritional information per 100g serving.
         The information includes calories, protein, carbohydrates, sugar, fat, and fiber.

Example:
    check_nutrition(["Halal beef", "lettuce", "potato"])
    -> Returns detailed nutritional breakdown for available ingredients.
"""
```'''
    mock_nutrition_db = {'Halal beef': {'calories': 250, 'protein': 26.0, 'carbs': 0.0, 'sugar': 0.0, 'fat': 15.0, 'fiber': 0.0}, 'Pita bread': {'calories': 275, 'protein': 9.0, 'carbs': 55.0, 'sugar': 2.0, 'fat': 1.0, 'fiber': 2.5}, 'Garlic sauce': {'calories': 180, 'protein': 2.0, 'carbs': 12.0, 'sugar': 8.0, 'fat': 14.0, 'fiber': 0.5}, 'Lettuce': {'calories': 15, 'protein': 1.4, 'carbs': 3.0, 'sugar': 1.8, 'fat': 0.2, 'fiber': 1.3}, 'Tomatoes': {'calories': 18, 'protein': 0.9, 'carbs': 3.9, 'sugar': 2.6, 'fat': 0.2, 'fiber': 1.2}, 'Cucumber': {'calories': 16, 'protein': 0.7, 'carbs': 4.0, 'sugar': 3.6, 'fat': 0.1, 'fiber': 0.5}, 'Spices': {'calories': 250, 'protein': 6.0, 'carbs': 65.0, 'sugar': 18.0, 'fat': 4.0, 'fiber': 25.0}, 'Basmati rice': {'calories': 350, 'protein': 7.0, 'carbs': 78.0, 'sugar': 0.1, 'fat': 0.6, 'fiber': 1.0}, 'Halal chicken': {'calories': 165, 'protein': 31.0, 'carbs': 0.0, 'sugar': 0.0, 'fat': 3.6, 'fiber': 0.0}, 'Onions': {'calories': 40, 'protein': 1.1, 'carbs': 9.3, 'sugar': 4.2, 'fat': 0.1, 'fiber': 1.7}, 'Yogurt': {'calories': 59, 'protein': 10.0, 'carbs': 3.6, 'sugar': 3.6, 'fat': 0.4, 'fiber': 0.0}, 'Ginger-garlic paste': {'calories': 125, 'protein': 6.0, 'carbs': 28.0, 'sugar': 15.0, 'fat': 1.0, 'fiber': 2.0}, 'Fresh coriander': {'calories': 23, 'protein': 2.1, 'carbs': 3.7, 'sugar': 0.9, 'fat': 0.5, 'fiber': 0.3}, 'Apple': {'calories': 52, 'protein': 0.3, 'carbs': 13.8, 'sugar': 10.4, 'fat': 0.2, 'fiber': 2.4}, 'Banana': {'calories': 89, 'protein': 1.1, 'carbs': 22.8, 'sugar': 12.2, 'fat': 0.3, 'fiber': 2.6}, 'Carrot': {'calories': 41, 'protein': 0.9, 'carbs': 9.6, 'sugar': 4.7, 'fat': 0.2, 'fiber': 2.8}, 'Broccoli': {'calories': 34, 'protein': 2.8, 'carbs': 6.6, 'sugar': 1.5, 'fat': 0.4, 'fiber': 2.6}, 'Oats': {'calories': 389, 'protein': 16.9, 'carbs': 66.3, 'sugar': 0.0, 'fat': 6.9, 'fiber': 10.6}}
    if not isinstance(ingredient_list, list) or not all((isinstance(item, str) for item in ingredient_list)):
        return "Error: 'ingredient_list' must be a list of strings."
    if not ingredient_list:
        return "Error: 'ingredient_list' cannot be empty."
    unique_ingredients = list(dict.fromkeys([ingredient.strip() for ingredient in ingredient_list if ingredient.strip()]))
    if not unique_ingredients:
        return 'Error: No valid ingredients provided.'
    available_ingredients_data = []
    for ingredient in unique_ingredients:
        matched_ingredient = None
        for db_ingredient in mock_nutrition_db:
            if ingredient.lower() == db_ingredient.lower():
                matched_ingredient = db_ingredient
                break
        if matched_ingredient:
            nutrition = mock_nutrition_db[matched_ingredient]
            available_ingredients_data.append({'name': matched_ingredient, 'nutrition': nutrition})
    if available_ingredients_data:
        output_lines = ['Available Ingredients with Nutritional Information (per 100g):']
        output_lines.append('')
        for item in available_ingredients_data:
            nutrition = item['nutrition']
            output_lines.append(f"{item['name']}:")
            output_lines.append(f"  Calories: {nutrition['calories']} cal")
            output_lines.append(f"  Protein: {nutrition['protein']}g")
            output_lines.append(f"  Carbohydrates: {nutrition['carbs']}g")
            output_lines.append(f"  Sugar: {nutrition['sugar']}g")
            output_lines.append(f"  Fat: {nutrition['fat']}g")
            output_lines.append(f"  Fiber: {nutrition['fiber']}g")
            output_lines.append('')
        return '\n'.join(output_lines)
    else:
        return 'No ingredients from your list are available in the database.'
if __name__ == '__main__':
    mcp.run(transport='stdio')