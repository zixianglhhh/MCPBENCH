from mcp.server.fastmcp import FastMCP
mcp = FastMCP('package_delivery_tracker')

@mcp.tool()
def package_delivery_tracker(tracking_number: str) -> str:
    '''"""
Provide the current status of a package by its tracking number.

The tool contains a small simulated carrier database with standardized status
codes. Each tracking number must exactly match one of the entries below. The
response includes the last known checkpoint, estimated delivery window, and the
carrier handling the shipment.

Args:
    tracking_number (str): Unique shipment identifier printed on the shipping label.

Returns:
    str: Status summary with location, timestamp, and ETA, or an error if unknown.
"""'''
    shipments = {
        '1Z999AA10123456784': {
            'carrier': 'UPS',
            'status': 'In Transit',
            'last_scan': 'Portland, OR Distribution Center',
            'timestamp': '10/31/2025 21:42',
            'eta': '11/02/2025',
        },
        '9400111899223951135987': {
            'carrier': 'USPS',
            'status': 'Out for Delivery',
            'last_scan': 'Seattle, WA Carrier Facility',
            'timestamp': '11/01/2025 07:15',
            'eta': '11/01/2025',
        },
        '786512345678': {
            'carrier': 'FedEx',
            'status': 'Delayed - Weather',
            'last_scan': 'Denver, CO Hub',
            'timestamp': '10/31/2025 18:05',
            'eta': '11/04/2025',
        },
        'JD000222333444555666': {
            'carrier': 'DHL',
            'status': 'Arrived at Destination Facility',
            'last_scan': 'Frankfurt, DE Gateway',
            'timestamp': '10/31/2025 12:50',
            'eta': '11/03/2025',
        },
    }
    if not tracking_number:
        return "Error: 'tracking_number' is required."
    record = shipments.get(tracking_number)
    if not record:
        return f"Error: Tracking number '{tracking_number}' not found."
    return (
        f"Carrier: {record['carrier']}\n"
        f"Status: {record['status']}\n"
        f"Last Scan: {record['last_scan']}\n"
        f"Timestamp: {record['timestamp']}\n"
        f"Estimated Delivery: {record['eta']}"
    )
if __name__ == '__main__':
    mcp.run(transport='stdio')
