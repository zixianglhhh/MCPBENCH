from mcp.server.fastmcp import FastMCP
from typing import List
mcp = FastMCP('get_realtime_market_data')

@mcp.tool()
def get_realtime_market_data(symbols: List[str], source: str, fields: List[str], market: str) -> str:
    '''```python
    """
    Fetch real-time market data snapshots for specified symbols.

    This function retrieves up-to-the-moment market data for a list of specified symbols, which can
    include equities, indices, or category tickers. The data is sourced from a specified provider and
    is intended for use in downstream analytics, such as sales or popularity trend modeling.

    Args:
        symbols (List[str]): A list of stock symbols, indices, or category tickers to fetch data for.
            Examples include ['AAPL', '600519.SS', 'LIQUOR_CAT'].
        source (str): The data source provider, such as 'yahoo', 'bloomberg', 'alpha_vantage', or 'custom_api'.
            This is used to construct the data storage link and identify the data origin.
        fields (List[str], optional): A list of specific fields to retrieve from the market data. If not provided,
            defaults to ['symbol', 'name', 'last', 'change', 'change_pct', 'volume', 'turnover', 'market_cap', 'timestamp'].
            Available fields include:
            - 'symbol': Stock symbol/ticker
            - 'name': Company name
            - 'last': Last traded price
            - 'change': Price change from previous close
            - 'change_pct': Percentage change
            - 'volume': Trading volume
            - 'turnover': Total turnover value
            - 'market_cap': Market capitalization
            - 'timestamp': Data timestamp
            - 'category': Industry category
        market (str): The market or exchange identifier, such as 'NYSE', 'NASDAQ', 'SSE', or 'SZSE'.
            This is used in constructing the data storage link.

    Returns:
        str: A URL linking to the data storage location where the fetched market data is stored.
            The link is constructed using the input parameters 'source' and 'market', formatted as:
            'https://{source}.marketdata.local/{market}/data'.

    Note:
        This function is designed to provide the freshest market numbers for analytics purposes and
        does not perform any data analysis or insight computation itself.
    """
```'''
    mock_market_snapshots = {('LIQUOR_CAT', 'yahoo'): {'symbol': 'LIQUOR_CAT', 'name': 'Liquor Industry Category Index', 'last': 3250.75, 'change': 15.2, 'change_pct': 0.47, 'volume': 4520000, 'turnover': 520000000.0, 'market_cap': None, 'timestamp': '2024-06-11T14:30:00+08:00', 'category': 'Liquor', 'source': 'yahoo', 'market': 'SSE'}, ('LIQUOR_CAT', 'xueqiu'): {'symbol': 'LIQUOR_CAT', 'name': '白酒行业指数', 'last': 3280.5, 'change': 18.75, 'change_pct': 0.57, 'volume': 4800000, 'turnover': 550000000.0, 'market_cap': None, 'timestamp': '2024-06-11T14:30:00+08:00', 'category': 'Liquor', 'source': 'xueqiu', 'market': 'CN'}, ('BANK_CAT', 'bloomberg'): {'symbol': 'BANK_CAT', 'name': 'Banking Industry Category Index', 'last': 980.2, 'change': -5.8, 'change_pct': -0.59, 'volume': 12800000, 'turnover': 1080000000.0, 'market_cap': None, 'timestamp': '2024-06-11T14:30:00+08:00', 'category': 'Banking', 'source': 'bloomberg', 'market': 'SZSE'}, ('BANK_CAT', 'xueqiu'): {'symbol': 'BANK_CAT', 'name': '银行行业指数', 'last': 975.8, 'change': -8.2, 'change_pct': -0.83, 'volume': 13500000, 'turnover': 1120000000.0, 'market_cap': None, 'timestamp': '2024-06-11T14:30:00+08:00', 'category': 'Banking', 'source': 'xueqiu', 'market': 'CN'}}
    if not isinstance(symbols, list) or not symbols:
        raise ValueError("Parameter 'symbols' must be a non-empty list of symbol strings.")
    if source is not None and (not isinstance(source, str)):
        raise ValueError("Parameter 'source' must be a string if provided.")
    if fields is not None and (not isinstance(fields, list) or not all((isinstance(f, str) for f in fields))):
        raise ValueError("Parameter 'fields' must be a list of strings if provided.")
    if market is not None and (not isinstance(market, str)):
        raise ValueError("Parameter 'market' must be a string if provided.")
    default_fields = ['symbol', 'name', 'last', 'change', 'change_pct', 'volume', 'turnover', 'market_cap', 'timestamp']
    fetched_data = {}
    for sym in symbols:
        snapshot = mock_market_snapshots.get((sym, source))
        if not snapshot:
            fetched_data[sym] = {'error': f'Symbol {sym} not found in {source} mock data.'}
            continue
        field_list = fields if fields else default_fields
        filtered_snapshot = {k: snapshot.get(k) for k in field_list if k in snapshot}
        filtered_snapshot['data_source'] = source
        filtered_snapshot['market'] = market
        fetched_data[sym] = filtered_snapshot
    import json
    mock_storage = {}
    mock_storage[f'{source}_{market}'] = fetched_data
    return f'https://{source}.marketdata.local/{market}_latest_snapshot.json'
if __name__ == '__main__':
    mcp.run(transport='stdio')