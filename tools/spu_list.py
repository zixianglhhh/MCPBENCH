from mcp.server.fastmcp import FastMCP
mcp = FastMCP('spu_list')

@mcp.tool()
def spu_list(brand: str) -> str:
    '''```python
    """
    Searches for product title information based on the provided brand term, 
    including detailed product information and specifications. The brand term 
    must not be empty.

    Args:
        brand (str): The search term used to find matching product titles. 
                     It should be a non-empty string. Brand should be exactly in lowercase.

    Returns:
        str: A formatted string containing the list of products that match the 
             brand term, including their titles, descriptions, and specifications. 
             If no products are found, a message indicating no matches is returned.
             If the brand is invalid, an error message is returned.
    """
```'''
    if not isinstance(brand, str) or not brand.strip():
        return "Error: 'brand' parameter cannot be empty."
    mock_product_db = {'toyota': [{'title': 'Toyota Corolla', 'info': 'Compact sedan, known for reliability and fuel efficiency.', 'specs': {'Engine': '1.8L I4', 'Transmission': 'CVT', 'Fuel Economy': '30/38 mpg'}}, {'title': 'Toyota Camry', 'info': 'Midsize sedan with a spacious interior and smooth ride.', 'specs': {'Engine': '2.5L I4 or 3.5L V6', 'Transmission': '8-speed automatic', 'Fuel Economy': '28/39 mpg'}}, {'title': 'Toyota RAV4', 'info': 'Compact SUV with great cargo space and optional AWD.', 'specs': {'Engine': '2.5L I4', 'Transmission': '8-speed automatic', 'Fuel Economy': '27/35 mpg'}}], 'honda': [{'title': 'Honda Civic', 'info': 'Popular compact car with sporty handling.', 'specs': {'Engine': '2.0L I4 or 1.5L Turbo', 'Transmission': 'CVT', 'Fuel Economy': '31/40 mpg'}}, {'title': 'Honda Accord', 'info': 'Midsize sedan with refined styling and advanced safety features.', 'specs': {'Engine': '1.5L Turbo I4 or 2.0L Turbo I4', 'Transmission': 'CVT or 10-speed automatic', 'Fuel Economy': '30/38 mpg'}}]}
    normalized_brand = brand.strip().lower()
    if normalized_brand in mock_product_db:
        products = mock_product_db[normalized_brand]
        output_lines = [f"Products for brand '{brand}':"]
        for p in products:
            output_lines.append(f"- {p['title']}: {p['info']}")
            for (spec_name, spec_value) in p['specs'].items():
                output_lines.append(f'    {spec_name}: {spec_value}')
        return '\n'.join(output_lines)
    matched_products = []
    for (brand, products) in mock_product_db.items():
        for p in products:
            if normalized_brand in p['title'].lower():
                matched_products.append(p)
    if matched_products:
        output_lines = [f"Products matching '{brand}':"]
        for p in matched_products:
            output_lines.append(f"- {p['title']}: {p['info']}")
            for (spec_name, spec_value) in p['specs'].items():
                output_lines.append(f'    {spec_name}: {spec_value}')
        return '\n'.join(output_lines)
    return f"No products found for brand '{brand}'."
if __name__ == '__main__':
    mcp.run(transport='stdio')