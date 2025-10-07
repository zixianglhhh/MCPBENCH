from mcp.server.fastmcp import FastMCP
mcp = FastMCP('search_stock_byname')

@mcp.tool()
def search_stock_byname(name: str) -> str:
    '''```python
    """
    Searches for stocks by name and returns a structured list of matching instruments.

    This function helps analysts quickly identify the correct stock by providing key 
    identifiers and metadata for each result. Typical return fields include the company 
    name, ticker symbol, and relevance score. This allows analysts to efficiently 
    proceed with requesting quotes, histories, or comprehensive analysis reports.

    Args:
        name (str): The name or ticker symbol of the stock to search for. This should 
            be a non-empty string.

    Returns:
        str: A formatted string containing a list of matching stocks with their company 
        name, ticker symbol, and relevance score. If no matches are found, a message 
        indicating no results will be returned.
    """
```'''
    mock_stock_db = [{'company_name': 'Alibaba Group Holding Limited', 'ticker': 'BABA', 'market': 'China', 'relevance_score': 0.95}, {'company_name': 'Tencent Holdings Limited', 'ticker': '0700.HK', 'market': 'China', 'relevance_score': 0.93}, {'company_name': 'JD.com, Inc.', 'ticker': 'JD', 'market': 'China', 'relevance_score': 0.9}, {'company_name': 'Meituan', 'ticker': '3690.HK', 'market': 'China', 'relevance_score': 0.88}, {'company_name': 'Pinduoduo Inc.', 'ticker': 'PDD', 'market': 'China', 'relevance_score': 0.87}, {'company_name': 'Apple Inc.', 'ticker': 'AAPL', 'market': 'US', 'relevance_score': 0.98}, {'company_name': 'Microsoft Corporation', 'ticker': 'MSFT', 'market': 'US', 'relevance_score': 0.97}, {'company_name': 'Alphabet Inc.', 'ticker': 'GOOGL', 'market': 'US', 'relevance_score': 0.96}, {'company_name': 'Tesla, Inc.', 'ticker': 'TSLA', 'market': 'US', 'relevance_score': 0.95}, {'company_name': 'NVIDIA Corporation', 'ticker': 'NVDA', 'market': 'US', 'relevance_score': 0.94}]
    if not isinstance(name, str) or not name.strip():
        return "Error: 'name' must be a non-empty string."
    name_lower = name.lower().strip()
    results = []
    for stock in mock_stock_db:
        if name_lower in stock['company_name'].lower() or name_lower in stock['ticker'].lower():
            results.append(stock)
    results.sort(key=lambda x: x['relevance_score'], reverse=True)
    results = results[:5]
    if not results:
        return f"No stocks found matching name '{name}'."
    output_lines = ['Search Results:']
    for r in results:
        output_lines.append(f"Company: {r['company_name']}, Ticker: {r['ticker']}, Relevance Score: {r['relevance_score']:.2f}")
    return '\n'.join(output_lines)
if __name__ == '__main__':
    mcp.run(transport='stdio')