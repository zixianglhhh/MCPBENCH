from mcp.server.fastmcp import FastMCP
mcp = FastMCP('get_market_summary')

@mcp.tool()
def get_market_summary(filter_type: list, filter_count: str, start_date: str, end_date: str) -> str:
    '''```python
"""
Retrieves a summary of KRW cryptocurrency markets with options to filter results based on popularity, visit frequency, and new listings.

Args:
    filter_type (list of str): A list of filter criteria to apply. Valid options are "popular", "most_visited", and "new_listing".
    filter_count (str): The number of results to return for each specified filter type. Must be a positive integer.
    start_date (str): The start date for filtering new listings, in the format 'YYYY-MM-DD'.
    end_date (str): The end date for filtering new listings, in the format 'YYYY-MM-DD'.

Returns:
    str: A formatted string containing the market summary with results filtered according to the specified criteria.
"""
```'''
    mock_market_data = [{'market': 'KRW-BTC', 'name': 'Bitcoin', 'volume_24h': 25000000000, 'visits': 120000, 'listed_days_ago': 1500, 'listing_date': '2021-01-01'}, {'market': 'KRW-ETH', 'name': 'Ethereum', 'volume_24h': 15000000000, 'visits': 95000, 'listed_days_ago': 1400, 'listing_date': '2021-02-01'}, {'market': 'KRW-XRP', 'name': 'Ripple', 'volume_24h': 8000000000, 'visits': 88000, 'listed_days_ago': 1300, 'listing_date': '2021-03-01'}, {'market': 'KRW-ADA', 'name': 'Cardano', 'volume_24h': 6000000000, 'visits': 72000, 'listed_days_ago': 1200, 'listing_date': '2021-04-01'}, {'market': 'KRW-DOGE', 'name': 'Dogecoin', 'volume_24h': 5500000000, 'visits': 68000, 'listed_days_ago': 1100, 'listing_date': '2021-05-01'}, {'market': 'KRW-SOL', 'name': 'Solana', 'volume_24h': 5000000000, 'visits': 64000, 'listed_days_ago': 100, 'listing_date': '2024-06-01'}, {'market': 'KRW-DOT', 'name': 'Polkadot', 'volume_24h': 4200000000, 'visits': 58000, 'listed_days_ago': 900, 'listing_date': '2021-07-01'}, {'market': 'KRW-MATIC', 'name': 'Polygon', 'volume_24h': 3800000000, 'visits': 55000, 'listed_days_ago': 800, 'listing_date': '2021-08-01'}, {'market': 'KRW-APT', 'name': 'Aptos', 'volume_24h': 3600000000, 'visits': 53000, 'listed_days_ago': 30, 'listing_date': '2025-08-28'}, {'market': 'KRW-ARB', 'name': 'Arbitrum', 'volume_24h': 3400000000, 'visits': 52000, 'listed_days_ago': 10, 'listing_date': '2025-09-17'}, {'market': 'KRW-SUI', 'name': 'Sui', 'volume_24h': 3200000000, 'visits': 48000, 'listed_days_ago': 5, 'listing_date': '2025-09-22'}, {'market': 'KRW-OP', 'name': 'Optimism', 'volume_24h': 3000000000, 'visits': 45000, 'listed_days_ago': 3, 'listing_date': '2025-09-24'}, {'market': 'KRW-BASE', 'name': 'Base', 'volume_24h': 2800000000, 'visits': 42000, 'listed_days_ago': 1, 'listing_date': '2025-09-26'}, {'market': 'KRW-LINK', 'name': 'Chainlink', 'volume_24h': 4500000000, 'visits': 62000, 'listed_days_ago': 800, 'listing_date': '2021-09-01'}, {'market': 'KRW-UNI', 'name': 'Uniswap', 'volume_24h': 4000000000, 'visits': 60000, 'listed_days_ago': 700, 'listing_date': '2021-10-01'}]
    try:
        filter_count_int = int(filter_count)
    except ValueError:
        return "Error: 'filter_count' must be a valid integer."
    if filter_count_int <= 0:
        return "Error: 'filter_count' must be greater than 0."
    valid_filters = ['popular', 'most_visited', 'new_listing']
    for filter_t in filter_type:
        if filter_t not in valid_filters:
            return f"Error: Invalid filter type '{filter_t}'. Must be one of {valid_filters}."
    from datetime import datetime
    try:
        start_dt = datetime.strptime(start_date, '%Y-%m-%d')
        end_dt = datetime.strptime(end_date, '%Y-%m-%d')
    except ValueError:
        return 'Error: Dates must be in YYYY-MM-DD format.'
    if start_dt > end_dt:
        return "Error: 'start_date' cannot be after 'end_date'."
    output_lines = []
    output_lines.append('KRW Market Summary:')
    output_lines.append('=' * 50)
    if 'popular' in filter_type:
        popular_data = sorted(mock_market_data, key=lambda x: x['volume_24h'], reverse=True)[:filter_count_int]
        output_lines.append(f'\nTop {filter_count_int} Popular Cryptocurrencies (by Volume):')
        for (i, coin) in enumerate(popular_data, 1):
            output_lines.append(f"{i}. {coin['name']} ({coin['market']}): ₩{coin['volume_24h']:,}")
    if 'most_visited' in filter_type:
        visited_data = sorted(mock_market_data, key=lambda x: x['visits'], reverse=True)[:filter_count_int]
        output_lines.append(f'\nTop {filter_count_int} Most Visited Coins:')
        for (i, coin) in enumerate(visited_data, 1):
            output_lines.append(f"{i}. {coin['name']} ({coin['market']}): {coin['visits']:,} visits")
    if 'new_listing' in filter_type:
        new_listings = []
        for coin in mock_market_data:
            coin_date = datetime.strptime(coin['listing_date'], '%Y-%m-%d')
            if start_dt <= coin_date <= end_dt:
                new_listings.append(coin)
        new_listings = sorted(new_listings, key=lambda x: x['listing_date'], reverse=True)[:filter_count_int]
        output_lines.append(f'\nNewly Listed Coins ({start_date} to {end_date}):')
        if new_listings:
            for (i, coin) in enumerate(new_listings, 1):
                output_lines.append(f"{i}. {coin['name']} ({coin['market']}): Listed on {coin['listing_date']}")
        else:
            output_lines.append('No new listings found in the specified date range.')
    return '\n'.join(output_lines)
if __name__ == '__main__':
    mcp.run(transport='stdio')