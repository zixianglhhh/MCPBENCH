from mcp.server.fastmcp import FastMCP
mcp = FastMCP('analyze_sales')

@mcp.tool()
def analyze_sales(input_data_link: str) -> str:
    '''```python
    """
    Analyzes category-level sales trends using provided market snapshots and/or sales data.

    This function calculates key performance indicators (KPIs) such as growth, momentum, 
    market share, and volatility for each category. It ranks categories based on growth 
    and provides concise insights to explain shifts in popularity. This function is 
    intended to be used after retrieving data with `get_realtime_market_data` and does 
    not fetch data itself.

    Args:
        input_data_link (str or None): A string representing the link to the input data 
            source. If None, default mock data is used for analysis.

    Returns:
        str: A formatted string containing the sales trend analysis, including KPIs for 
        each category and insights on the top and bottom performers.
    """
```'''
    mock_market_snapshots = {'latest_snapshot': {'Electronics': {'sales': [120000, 125000, 132000, 150000], 'market_share': 0.35}, 'Home & Kitchen': {'sales': [80000, 85000, 87000, 90000], 'market_share': 0.25}, 'Fashion': {'sales': [60000, 62000, 61000, 65000], 'market_share': 0.2}, 'Sports': {'sales': [40000, 45000, 47000, 50000], 'market_share': 0.1}, 'Books': {'sales': [30000, 29000, 28000, 27000], 'market_share': 0.1}}}
    if input_data_link is not None and (not isinstance(input_data_link, str)):
        return "Error: 'input_data_link' must be a string or None."
    sales_data = mock_market_snapshots.get('latest_snapshot')
    if not sales_data:
        return 'Error: No sales data available for analysis.'
    analysis_results = {}
    for (category, data) in sales_data.items():
        sales = data['sales']
        market_share = data['market_share']
        if len(sales) < 2:
            return f"Error: Not enough sales history for category '{category}'."
        growth = (sales[-1] - sales[0]) / sales[0] * 100
        monthly_growth_rates = [(sales[i] - sales[i - 1]) / sales[i - 1] * 100 for i in range(1, len(sales))]
        momentum = sum(monthly_growth_rates) / len(monthly_growth_rates)
        mean_growth = momentum
        variance = sum(((g - mean_growth) ** 2 for g in monthly_growth_rates)) / len(monthly_growth_rates)
        volatility = variance ** 0.5
        analysis_results[category] = {'growth_%': round(growth, 2), 'momentum_%': round(momentum, 2), 'market_share_%': round(market_share * 100, 2), 'volatility_%': round(volatility, 2)}
    ranked_by_growth = sorted(analysis_results.items(), key=lambda x: x[1]['growth_%'], reverse=True)
    insights = []
    (top_category, top_metrics) = ranked_by_growth[0]
    (bottom_category, bottom_metrics) = ranked_by_growth[-1]
    insights.append(f"'{top_category}' is leading in growth ({top_metrics['growth_%']}%), driven by strong momentum.")
    insights.append(f"'{bottom_category}' is losing popularity with a decline of {bottom_metrics['growth_%']}%.")
    output_lines = ['Sales Trend Analysis (Category-Level KPIs):']
    for (category, metrics) in analysis_results.items():
        output_lines.append(f"- {category}: Growth={metrics['growth_%']}%, Momentum={metrics['momentum_%']}%, Share={metrics['market_share_%']}%, Volatility={metrics['volatility_%']}%")
    output_lines.append('\nInsights:')
    output_lines.extend(insights)
    return '\n'.join(output_lines)
if __name__ == '__main__':
    mcp.run(transport='stdio')