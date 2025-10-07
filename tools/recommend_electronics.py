from mcp.server.fastmcp import FastMCP
mcp = FastMCP('recommend_electronics')

@mcp.tool()
def recommend_electronics(product_type: str) -> str:
    '''```python
    """
    Provides detailed information about electronics products, focusing on laptops with high-performance specifications and superior display quality.

    Args:
        product_type (str): The type of product to retrieve information for. Supported values include "laptop" and "iphone_16".

    Returns:
        str: A formatted string containing detailed information about the specified product type. This includes specifications, features, price range, and availability. If the product type is not found or invalid, an error message is returned.
    """
```'''
    mock_products_db = {'laptop': [{'name': 'Dell XPS 15 OLED', 'category': 'Laptop', 'specs': {'processor': 'Intel Core i9-13900H', 'ram': '32GB DDR5', 'storage': '1TB NVMe SSD', 'gpu': 'NVIDIA GeForce RTX 4070', 'display': '15.6-inch 4K OLED Touch, 100% AdobeRGB', 'weight': '1.9 kg', 'battery': '86Wh, up to 12 hours'}, 'features': ['Excellent color accuracy for design work', 'Premium build quality', 'Multiple Thunderbolt 4 ports', 'Wi-Fi 6E support'], 'price_range': '$2,199 - $2,499', 'availability': 'In stock at major retailers'}, {'name': 'MacBook Pro 16-inch M3 Max', 'category': 'Laptop', 'specs': {'processor': 'Apple M3 Max (12-core CPU, 30-core GPU)', 'ram': '36GB unified memory', 'storage': '1TB SSD', 'gpu': '30-core GPU', 'display': '16.2-inch Liquid Retina XDR, 1000 nits sustained brightness', 'weight': '2.16 kg', 'battery': 'Up to 22 hours'}, 'features': ['Exceptional performance for creative work', 'Outstanding display with ProMotion 120Hz', 'Excellent battery life', 'Silent operation under load'], 'price_range': '$3,199 - $3,999', 'availability': 'Available through Apple Store'}, {'name': 'ASUS ROG Zephyrus G14', 'category': 'Laptop', 'specs': {'processor': 'AMD Ryzen 9 7940HS', 'ram': '32GB DDR5', 'storage': '1TB NVMe SSD', 'gpu': 'NVIDIA GeForce RTX 4060', 'display': '14-inch QHD+ 165Hz, 100% DCI-P3', 'weight': '1.65 kg', 'battery': '76Wh, up to 8 hours'}, 'features': ['High refresh rate display for gaming', 'Compact and portable design', 'Excellent color accuracy', 'AniMe Matrix LED display on lid'], 'price_range': '$1,599 - $1,899', 'availability': 'In stock at electronics retailers'}, {'name': 'HP Spectre x360 16', 'category': 'Laptop', 'specs': {'processor': 'Intel Core i7-13700H', 'ram': '16GB DDR5', 'storage': '512GB NVMe SSD', 'gpu': 'Intel Arc A370M', 'display': '16-inch 3K+ OLED Touch, 100% DCI-P3', 'weight': '2.0 kg', 'battery': '83Wh, up to 10 hours'}, 'features': ['2-in-1 convertible design', 'Stunning OLED display', 'Premium build with gem-cut design', 'Bang & Olufsen speakers'], 'price_range': '$1,699 - $1,999', 'availability': 'Available at HP and major retailers'}], 'iphone_16': {'name': 'Apple iPhone 16 Pro Max', 'category': 'Smartphone', 'specs': {'processor': 'Apple A18 Pro', 'ram': '8GB', 'storage_options': ['256GB', '512GB', '1TB'], 'display': '6.9-inch Super Retina XDR OLED, ProMotion 120Hz', 'camera': 'Triple-lens system with 48MP main, 12MP ultra-wproduct_typee, 12MP telephoto', 'battery': 'Up to 28 hours vproduct_typeeo playback', 'connectivity': '5G, Wi‑Fi 6E, Bluetooth 5.3'}, 'features': ['Titanium frame', 'New periscope zoom lens', 'Advanced computational photography', 'USB-C with Thunderbolt support'], 'price_range': '$1,199 - $1,699 depending on storage', 'availability': 'Available through Apple Store and authorized resellers'}}
    if not isinstance(product_type, str) or not product_type.strip():
        return "Error: 'product_type' must be a non-empty string."
    products = mock_products_db.get(product_type)
    if not products:
        return f"Error: No product found with product_type '{product_type}'."
    if isinstance(products, list):
        details = 'Laptop Recommendations with Performance Specifications and Good Display Quality:\n'
        details += '=' * 80 + '\n\n'
        for (i, product) in enumerate(products, 1):
            details += f"{i}. {product['name']}\n"
            details += f"Category: {product['category']}\n"
            details += 'Specifications:\n'
            for (spec_key, spec_value) in product['specs'].items():
                details += f'  - {spec_key.capitalize()}: {spec_value}\n'
            details += 'Features:\n'
            for feature in product['features']:
                details += f'  - {feature}\n'
            details += f"Price Range: {product['price_range']}\n"
            details += f"Availability: {product['availability']}\n"
            details += '\n' + '-' * 60 + '\n\n'
    else:
        details = f"Product Name: {products['name']}\n"
        details += f"Category: {products['category']}\n"
        details += 'Specifications:\n'
        for (spec_key, spec_value) in products['specs'].items():
            details += f'  - {spec_key.capitalize()}: {spec_value}\n'
        details += 'Features:\n'
        for feature in products['features']:
            details += f'  - {feature}\n'
        details += f"Price Range: {products['price_range']}\n"
        details += f"Availability: {products['availability']}"
    return details
if __name__ == '__main__':
    mcp.run(transport='stdio')