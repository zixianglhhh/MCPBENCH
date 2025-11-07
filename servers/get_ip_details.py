from mcp.server.fastmcp import FastMCP
from typing import List
mcp = FastMCP('get_ip_details')

@mcp.tool()
def get_ip_details(ip_address: List[str]) -> str:
    '''```python
"""
Retrieve detailed information about IP addresses, including geolocation data.

This function accepts a list of IP addresses and returns detailed information 
for each, including the country, region, city, and timezone. It validates the 
format of each IP address and provides an error message for any invalid entries.

Args:
    ip_address (List[str]): A non-empty list of IP address strings to be 
    processed. Each IP address should be a valid IPv4 or IPv6 format.

Returns:
    str: A formatted string containing geolocation details for each valid IP 
    address. If an IP address is invalid or no data is found, an error message 
    is returned.
"""
```'''
    mock_ip_db = {'203.0.113.25': {'ip': '203.0.113.25', 'country': 'United States', 'region': 'New York', 'city': 'New York City', 'timezone': 'America/New_York'}, '198.51.100.42': {'ip': '198.51.100.42', 'country': 'United Kingdom', 'region': 'England', 'city': 'London', 'timezone': 'Europe/London'}, '192.0.2.88': {'ip': '192.0.2.88', 'country': 'Japan', 'region': 'Tokyo', 'city': 'Tokyo', 'timezone': 'Asia/Tokyo'}}
    import re

    def is_valid_ip(ip):
        ipv4_pattern = '^\\d{1,3}(\\.\\d{1,3}){3}$'
        ipv6_pattern = '^([0-9a-fA-F]{0,4}:){2,7}[0-9a-fA-F]{0,4}$'
        return bool(re.match(ipv4_pattern, ip)) or bool(re.match(ipv6_pattern, ip))
    if not ip_address or not isinstance(ip_address, list):
        return "Error: 'ip_address' parameter must be a non-empty list of strings."
    invalid_ips = []
    for ip in ip_address:
        if not isinstance(ip, str) or not is_valid_ip(ip):
            invalid_ips.append(ip)
    if invalid_ips:
        return f"Error: Invalid IP addresses found: {', '.join(invalid_ips)}"
    results = []
    for ip in ip_address:
        if ip in mock_ip_db:
            ip_info = mock_ip_db[ip]
            result = f"IP Address: {ip_info['ip']}\nCountry: {ip_info['country']}\nRegion: {ip_info['region']}\nCity: {ip_info['city']}\nTimezone: {ip_info['timezone']}"
            results.append(result)
        else:
            results.append(f"No geolocation data found for IP address '{ip}'.")
    return '\n\n'.join(results)
if __name__ == '__main__':
    mcp.run(transport='stdio')