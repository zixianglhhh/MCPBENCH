from mcp.server.fastmcp import FastMCP
mcp = FastMCP('home_appliance_warranty_lookup')

@mcp.tool()
def home_appliance_warranty_lookup(serial_number: str) -> str:
    '''"""
Check warranty coverage and service phone numbers for major appliances.

Only serial numbers in the table below are recognized. The response indicates
coverage status, expiration date, and the appropriate service hotline.

Args:
    serial_number (str): Manufacturer serial printed on the appliance label.

Returns:
    str: Warranty summary or an error when the serial number is unregistered.
"""'''
    warranties = {
        'WMX-449201': {'product': 'Front-Load Washer', 'status': 'Active', 'expires': '2026-02-14', 'support': '1-800-555-0191'},
        'FRG-220198': {'product': 'French Door Refrigerator', 'status': 'Expired', 'expires': '2024-09-30', 'support': '1-800-555-0142'},
        'DWS-772310': {'product': 'Dishwasher', 'status': 'Active', 'expires': '2025-12-01', 'support': '1-800-555-0168'},
        'HVAC-903311': {'product': 'Heat Pump', 'status': 'Active', 'expires': '2028-08-19', 'support': '1-800-555-0110'},
    }
    if not serial_number:
        return "Error: 'serial_number' is required."
    record = warranties.get(serial_number.upper())
    if not record:
        return f"Error: Serial number '{serial_number}' not found."
    return (
        f"Product: {record['product']}\n"
        f"Warranty Status: {record['status']}\n"
        f"Expiration Date: {record['expires']}\n"
        f"Service Hotline: {record['support']}"
    )
if __name__ == '__main__':
    mcp.run(transport='stdio')
