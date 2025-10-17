from mcp.server.fastmcp import FastMCP
mcp = FastMCP('get_markets')

@mcp.tool()
def get_markets(exchange: str) -> str:
    '''```python
    """
    Retrieve a list of all market codes supported by Upbit for trading.

    Args:
        exchange (str): The name of the exchange to query. If None, defaults to 'Upbit'.

    Returns:
        str: A formatted string listing all supported markets for the specified exchange,
             including details such as base currency, quote currency, popularity, and 
             whether it is a new listing. Returns an error message if the exchange is 
             not a string or is not found in the supported data.
    """
```'''
    mock_market_data = {'Upbit': [{'market': 'KRW-BTC', 'base_currency': 'BTC', 'quote_currency': 'KRW', 'status': 'active', 'popularity': 'high', 'new_listing': False}, {'market': 'KRW-ETH', 'base_currency': 'ETH', 'quote_currency': 'KRW', 'status': 'active', 'popularity': 'high', 'new_listing': False}, {'market': 'KRW-XRP', 'base_currency': 'XRP', 'quote_currency': 'KRW', 'status': 'active', 'popularity': 'medium', 'new_listing': False}, {'market': 'KRW-APT', 'base_currency': 'APT', 'quote_currency': 'KRW', 'status': 'active', 'popularity': 'emerging', 'new_listing': True}, {'market': 'KRW-SAND', 'base_currency': 'SAND', 'quote_currency': 'KRW', 'status': 'active', 'popularity': 'medium', 'new_listing': True}, {'market': 'BTC-ETH', 'base_currency': 'ETH', 'quote_currency': 'BTC', 'status': 'active', 'popularity': 'high', 'new_listing': False}]}
    if exchange is not None:
        if not isinstance(exchange, str):
            return "Error: 'exchange' parameter must be a string."
        if exchange not in mock_market_data:
            return f"Error: Exchange '{exchange}' not found in supported mock data."
    selected_exchange = exchange if exchange else 'Upbit'
    markets = mock_market_data[selected_exchange]
    output_lines = [f'Supported markets for {selected_exchange}:']
    for m in markets:
        new_tag = ' (New Listing)' if m['new_listing'] else ''
        output_lines.append(f"- {m['market']} | Base: {m['base_currency']}, Quote: {m['quote_currency']}, Popularity: {m['popularity']}{new_tag}")
    return '\n'.join(output_lines)
if __name__ == '__main__':
    mcp.run(transport='stdio')