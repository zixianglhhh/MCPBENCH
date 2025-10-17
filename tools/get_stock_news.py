from mcp.server.fastmcp import FastMCP
'\nfor example if in the tasks mentioned Shanghai Stock Exchange Composite Index or Shenzhen Stock Exchange Component Index, you should use the ticker "SSEC" or "SZCOMP" to get the news.\n'
mcp = FastMCP('get_stock_news')

@mcp.tool()
def get_stock_news(ticker: str, max_result: int) -> str:
    '''```python
    """
    Retrieve the latest financial news articles related to a specific stock symbol or ticker.

    This function fetches and returns headlines, sources, publication dates, and article summaries
    for a given stock ticker. It helps users connect recent market movements with relevant news coverage.

    Args:
        ticker (str): The stock symbol or ticker for which to retrieve news articles. Must be a non-empty string.
            Valid tickers include: 'AAPL' (Apple Inc.), 'SSEC' (Shanghai Stock Exchange Composite Index),
            'SZCOMP' (Shenzhen Component Index). use the simple ticker codes.
        max_result (int): The maximum number of news articles to retrieve. Must be a positive integer. Defaults to 10 if not provided.

    Returns:
        str: A formatted string containing the latest news articles for the specified ticker, including headlines,
        sources, publication dates, and summaries. If no articles are found or if input validation fails, an error message is returned.
    """
```'''
    mock_news_db = {'AAPL': [{'headline': 'Apple Unveils New AI Features for iOS', 'source': 'TechCrunch', 'date': '2024-06-03', 'summary': 'Apple announced a range of AI-powered functionalities for its mobile operating system, aimed at boosting productivity.'}, {'headline': 'Apple Stock Rises Ahead of WWDC', 'source': 'Bloomberg', 'date': '2024-06-02', 'summary': 'Investors show optimism as Apple prepares to reveal new hardware and software updates.'}], 'SSEC': [{'headline': 'Shanghai Composite Rallies on Stimulus Hopes', 'source': 'Reuters', 'date': '2024-06-03', 'summary': 'The index surged over 2% as traders anticipated new government measures to boost the economy.'}, {'headline': 'Tech Stocks Lead Gains in Shanghai', 'source': 'Caixin', 'date': '2024-06-02', 'summary': 'Technology and consumer sectors drove the index higher amid positive earnings reports.'}], 'SZCOMP': [{'headline': 'Shenzhen Component Climbs on Manufacturing Data', 'source': 'South China Morning Post', 'date': '2024-06-03', 'summary': "Latest PMI data showed expansion in China's manufacturing sector, driving investor optimism."}, {'headline': 'New Energy Stocks Power Shenzhen Index', 'source': 'China Daily', 'date': '2024-06-01', 'summary': 'The surge in electric vehicle and battery firms boosted the overall index performance.'}]}
    if not isinstance(ticker, str) or not ticker.strip():
        return "Error: 'ticker' must be a non-empty string."
    if max_result is not None and (not isinstance(max_result, int) or max_result <= 0):
        return "Error: 'max_result' must be a positive integer if provided."
    if max_result is None:
        max_result = 10
    ticker_upper = ticker.strip().upper()
    if ticker_upper not in mock_news_db:
        return f"No news articles found for ticker '{ticker_upper}'."
    articles = mock_news_db[ticker_upper][:max_result]
    output_lines = [f'Latest news for {ticker_upper}:']
    for (i, article) in enumerate(articles, start=1):
        output_lines.append(f"{i}. {article['headline']} ({article['source']}, {article['date']})\n   Summary: {article['summary']}")
    return '\n'.join(output_lines)
if __name__ == '__main__':
    mcp.run(transport='stdio')