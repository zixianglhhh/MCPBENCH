from mcp.server.fastmcp import FastMCP
mcp = FastMCP('get_comprehensive_analysis')

@mcp.tool()
def get_comprehensive_analysis(symbol: str) -> str:
    '''```python
    """
    Retrieve a comprehensive analysis for a given stock symbol.

    Args:
        symbol (str): The stock symbol for which the comprehensive analysis 
            is requested. Must be a non-empty string.

    Returns:
        str: A detailed analysis report for the specified stock symbol, 
        including sector information, recent trends, performance metrics, 
        key reasons influencing the stock, and investment advice. 
        Returns an error message if the symbol is invalid or if no analysis 
        is found for the symbol.
    """
```'''
    mock_analysis_db = {'600519': {'name': 'Kweichow Moutai', 'sector': 'Liquor', 'recent_trend': 'Uptrend with strong momentum over the last quarter', 'performance': 'Stock price increased by 12% in the past month, outperforming the sector average', 'reasons': ['Strong domestic demand for premium liquor products', 'Robust financial results with revenue growth of 15% YoY', 'Positive market sentiment towards consumer staples', 'Expansion in e-commerce sales channels', 'Stable macroeconomic environment supporting consumer spending'], 'investment_advice': 'Consider accumulating positions on dips; long-term growth potential remains strong.'}, '000858': {'name': 'Wuliangye Yibin', 'sector': 'Liquor', 'recent_trend': 'Steady growth supported by high-end liquor demand', 'performance': 'Gained 8% in the last month', 'reasons': ['Continued brand strength in premium liquor market', 'Improved distribution network efficiency', 'Positive earnings surprise in last quarter'], 'investment_advice': 'Hold for steady returns; potential upside if consumer confidence remains high.'}, '601318': {'name': 'Ping An Insurance', 'sector': 'Insurance', 'recent_trend': 'Moderate recovery after earlier weakness', 'performance': 'Up 5% in the last month', 'reasons': ['Improved investment portfolio returns', 'Growth in life insurance premiums', 'Market optimism about financial sector reforms'], 'investment_advice': 'Good for diversified portfolios seeking financial sector exposure.'}, '300750': {'name': 'CATL', 'sector': 'Battery Manufacturing', 'recent_trend': 'Strong rebound driven by EV market optimism', 'performance': 'Up 15% in the last month', 'reasons': ['Increased EV battery orders', 'Partnership with major global car makers', 'Government policies supporting clean energy'], 'investment_advice': 'Buy on momentum; high growth potential but watch for valuation risks.'}, '002594': {'name': 'BYD Company', 'sector': 'Automotive / EV', 'recent_trend': 'Sustained rally due to strong sales figures', 'performance': 'Up 10% in the last month', 'reasons': ['Record-breaking EV sales', 'Expansion into foreign markets', 'Positive outlook on global EV adoption'], 'investment_advice': 'Accumulate for long-term EV sector exposure.'}}
    if not isinstance(symbol, str) or not symbol.strip():
        return "Error: 'symbol' must be a non-empty string."
    analysis = mock_analysis_db.get(symbol)
    if not analysis:
        return f"Error: No comprehensive analysis found for symbol '{symbol}'."
    result_lines = [f"Comprehensive Analysis for {analysis['name']} ({symbol}):", f"Sector: {analysis['sector']}", f"Recent Trend: {analysis['recent_trend']}", f"Performance: {analysis['performance']}", 'Key Reasons:']
    for (idx, reason) in enumerate(analysis['reasons'], start=1):
        result_lines.append(f'  {idx}. {reason}')
    result_lines.append(f"Investment Advice: {analysis['investment_advice']}")
    return '\n'.join(result_lines)
if __name__ == '__main__':
    mcp.run(transport='stdio')