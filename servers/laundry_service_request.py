from mcp.server.fastmcp import FastMCP
from typing import Literal
mcp = FastMCP('laundry_service_request')

@mcp.tool()
def laundry_service_request(customer_id: str, pickup_date: str, service_type: Literal['wash_fold', 'dry_cleaning', 'press_only']) -> str:
    '''"""
Submit a pickup request for a laundry service.

Pickup windows are validated against service availability. Different service
categories have separate turn-around times. All dates must use `YYYY-MM-DD`.

Args:
    customer_id (str): Registered customer identifier.
    pickup_date (str): Requested pickup date in `YYYY-MM-DD` format.
    service_type (Literal['wash_fold', 'dry_cleaning', 'press_only']): Desired service option.

Returns:
    str: Confirmation with drop-off estimate or an error message when unavailable.
"""'''
    availability = {
        'wash_fold': {'2025-11-01': True, '2025-11-03': True, '2025-11-05': False},
        'dry_cleaning': {'2025-11-01': False, '2025-11-02': True, '2025-11-04': True},
        'press_only': {'2025-11-02': True, '2025-11-03': True, '2025-11-06': True},
    }
    turnaround_hours = {'wash_fold': 24, 'dry_cleaning': 48, 'press_only': 12}
    if not customer_id:
        return "Error: 'customer_id' is required."
    if not pickup_date:
        return "Error: 'pickup_date' is required."
    if service_type not in availability:
        return "Error: Unsupported service type."
    service_calendar = availability[service_type]
    if pickup_date not in service_calendar or not service_calendar[pickup_date]:
        return f"Error: {service_type} is fully booked on {pickup_date}."
    return (
        f"Laundry pickup scheduled!\n"
        f"Customer: {customer_id}\n"
        f"Service: {service_type}\n"
        f"Pickup Date: {pickup_date}\n"
        f"Estimated Completion: {turnaround_hours[service_type]} hour(s) after pickup"
    )
if __name__ == '__main__':
    mcp.run(transport='stdio')
