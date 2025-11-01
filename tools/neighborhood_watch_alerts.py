from mcp.server.fastmcp import FastMCP
mcp = FastMCP('neighborhood_watch_alerts')

@mcp.tool()
def neighborhood_watch_alerts(zone: str, severity: str='all') -> str:
    '''"""
List the most recent neighborhood watch alerts for a patrol zone.

Zones correspond to homeowner association sectors. Severity may be filtered by
`info`, `caution`, or `urgent`. By default, all severities are returned.

Args:
    zone (str): Neighborhood zone identifier (e.g., "NW-5").
    severity (str): Optional severity filter. One of `info`, `caution`, `urgent`, or `all`.

Returns:
    str: Formatted alert messages ordered from newest to oldest.
"""'''
    alerts = {
        'NW-1': [
            {'severity': 'info', 'timestamp': '2025-10-31 20:05', 'message': 'Community meeting moved indoors.'},
            {'severity': 'urgent', 'timestamp': '2025-10-30 23:18', 'message': 'Report of suspicious vehicle near Elm St.'},
        ],
        'NW-3': [
            {'severity': 'caution', 'timestamp': '2025-11-01 06:45', 'message': 'Coyotes spotted near the playground.'},
            {'severity': 'info', 'timestamp': '2025-10-29 19:20', 'message': 'Streetlights on Maple Ave restored.'},
        ],
        'NW-5': [
            {'severity': 'urgent', 'timestamp': '2025-10-28 22:40', 'message': 'Car break-in reported on Pine Ct.'},
        ],
    }
    if not zone:
        return "Error: 'zone' is required."
    normalized_zone = zone.upper()
    if severity not in ['info', 'caution', 'urgent', 'all']:
        return "Error: Invalid severity filter."
    zone_alerts = alerts.get(normalized_zone)
    if not zone_alerts:
        return f"No alerts recorded for zone {normalized_zone}."
    filtered = [a for a in zone_alerts if severity == 'all' or a['severity'] == severity]
    if not filtered:
        return f"No alerts matching severity '{severity}' in zone {normalized_zone}."
    lines = [f"[{entry['timestamp']}] ({entry['severity'].upper()}) {entry['message']}" for entry in filtered]
    return "\n".join(lines)
if __name__ == '__main__':
    mcp.run(transport='stdio')
