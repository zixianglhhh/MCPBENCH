from mcp.server.fastmcp import FastMCP
mcp = FastMCP('home_energy_usage_report')

@mcp.tool()
def home_energy_usage_report(meter_id: str, billing_cycle: str) -> str:
    '''"""
Provide kWh consumption and cost estimates for a billing cycle.

The dataset includes smart meter readings aggregated by month. Billing cycle must
follow `YYYY-MM`. The tool returns usage, projected bill, and comparison to the
previous month.

Args:
    meter_id (str): Smart meter identifier tied to the household account.
    billing_cycle (str): Billing period in `YYYY-MM` format.

Returns:
    str: Usage report or a descriptive error when no data exists.
"""'''
    usage_history = {
        'MTR-2211': {
            '2025-09': {'kwh': 612, 'cost': 88.45},
            '2025-10': {'kwh': 578, 'cost': 83.12},
        },
        'MTR-9087': {
            '2025-10': {'kwh': 742, 'cost': 109.28},
            '2025-11': {'kwh': 705, 'cost': 103.54},
        },
        'MTR-3344': {
            '2025-08': {'kwh': 455, 'cost': 67.80},
            '2025-09': {'kwh': 498, 'cost': 72.15},
        },
    }
    if not meter_id:
        return "Error: 'meter_id' is required."
    if not billing_cycle:
        return "Error: 'billing_cycle' is required."
    account = usage_history.get(meter_id.upper())
    if not account:
        return f"Error: Meter '{meter_id}' not found."
    current = account.get(billing_cycle)
    if not current:
        return f"No usage recorded for {billing_cycle}."
    year, month = billing_cycle.split('-')
    prev_month = f"{year}-{int(month) - 1:02d}" if int(month) > 1 else None
    previous = account.get(prev_month) if prev_month else None
    comparison = ''
    if previous:
        delta = current['kwh'] - previous['kwh']
        trend = 'higher' if delta > 0 else 'lower'
        comparison = f"\nChange vs previous month: {abs(delta)} kWh {trend}."
    return (
        f"Usage for {billing_cycle}: {current['kwh']} kWh\n"
        f"Estimated Cost: ${current['cost']:.2f}" + comparison
    )
if __name__ == '__main__':
    mcp.run(transport='stdio')
