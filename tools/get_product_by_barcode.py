from mcp.server.fastmcp import FastMCP
mcp = FastMCP('get_product_by_barcode')

@mcp.tool()
def get_product_by_barcode(barcode: list) -> str:
    '''```python
"""
Retrieves detailed information about food products using their barcodes.

This function accepts a list of barcodes and returns detailed information for each corresponding product. 
If a barcode is invalid or not found, an appropriate error message is returned.

Args:
    barcode (list of str): A list of barcodes as strings to look up product information.

Returns:
    str: A formatted string containing detailed information for each product found, or error messages 
    for barcodes that are invalid or not found.
"""
```'''
    mock_products_db = {'4902102079290': {'name': 'Salalad Dressing', 'brand': 'Kewpie', 'category': 'Salad Dressing', 'ingredients': ['Soybean oil', 'Vinegar', 'Egg yolk', 'Sugar', 'Salt', 'Mustard', 'Spices'], 'nutrition_facts': {'serving_size': '15ml', 'calories': 60, 'fat': '6g', 'carbohydrates': '1g', 'protein': '0g'}, 'origin': 'Japan', 'description': 'A light and tangy Japanese-style salad dressing that pairs well with fresh vegetables.'}, '0737628064502': {'name': 'Organic Seaweed Snack', 'brand': "Annie Chun's", 'category': 'Snack', 'ingredients': ['Seaweed', 'Sunflower oil', 'Sesame oil', 'Salt'], 'nutrition_facts': {'serving_size': '5g', 'calories': 25, 'fat': '2g', 'carbohydrates': '1g', 'protein': '1g'}, 'origin': 'South Korea', 'description': 'Crispy, roasted organic seaweed sheets with a hint of sesame flavor.'}, '8410076471305': {'name': 'Dark Chocolate 70%', 'brand': 'Lindt', 'category': 'Chocolate', 'ingredients': ['Cocoa mass', 'Sugar', 'Cocoa butter', 'Vanilla extract'], 'nutrition_facts': {'serving_size': '40g', 'calories': 240, 'fat': '18g', 'carbohydrates': '15g', 'protein': '3g'}, 'origin': 'Switzerland', 'description': 'Rich and smooth dark chocolate with 70% cocoa content.'}}
    if not isinstance(barcode, list) or not barcode:
        return 'Error: Invalid input. Please provide a non-empty list of barcodes.'
    all_results = []
    for barcode_item in barcode:
        if not isinstance(barcode_item, str) or not barcode_item.strip():
            all_results.append(f"Error: Invalid barcode '{barcode_item}' - must be a non-empty string.")
            continue
        product_info = mock_products_db.get(barcode_item.strip())
        if not product_info:
            all_results.append(f'No product found for barcode: {barcode_item}. Please check the barcode and try again.')
            continue
        product_output = f"Barcode: {barcode_item}\nProduct Name: {product_info['name']}\nBrand: {product_info['brand']}\nCategory: {product_info['category']}\nOrigin: {product_info['origin']}\nDescription: {product_info['description']}\nIngredients: {', '.join(product_info['ingredients'])}\nNutrition Facts (per {product_info['nutrition_facts']['serving_size']}):\n  Calories: {product_info['nutrition_facts']['calories']}\n  Fat: {product_info['nutrition_facts']['fat']}\n  Carbohydrates: {product_info['nutrition_facts']['carbohydrates']}\n  Protein: {product_info['nutrition_facts']['protein']}"
        all_results.append(product_output)
    return '\n\n' + '=' * 80 + '\n\n'.join(all_results)
if __name__ == '__main__':
    mcp.run(transport='stdio')