from mcp.server.fastmcp import FastMCP
from typing import List
mcp = FastMCP('get_market_index')

@mcp.tool()
def get_market_index(indices: List[str]) -> str:
    '''```python
    """
    Retrieve data for specified major stock indices.

    This function provides information on major stock indices such as the 
    Shanghai Stock Exchange Index, Shenzhen Stock Exchange Component Index, 
    ChiNext Index, STAR Market 50, CSI 300, and CSI 500. It returns the latest 
    closing values, daily changes, percentage changes, and market trends for 
    the requested indices.

    Args:
        indices (List[str]): A list of index codes representing the stock 
            indices for which data is requested. Valid index codes include:
            'SHCOMP' (Shanghai Composite Index), 'SZCOMP' (Shenzhen Component Index),
            'STAR50' (STAR Market 50 Index), 'CSI300' (CSI 300 Index), 'CSI500' (CSI 500 Index).
            If None, data for all available indices will be returned.

    Returns:
        str: A formatted string containing the latest data for each requested 
        index, including the index name, latest closing value, change, 
        percentage change, trend, and the date of the data.
    """
```'''
    mock_indices_data = {'SHCOMP': {'name': 'Shanghai Composite Index', 'latest_close': 3225.14, 'change': -0.42, 'change_percent': -0.013, 'trend': 'slight downward in recent sessions due to profit-taking after a short rally', 'date': '2024-06-10'}, 'SZCOMP': {'name': 'Shenzhen Component Index', 'latest_close': 10875.56, 'change': 0.78, 'change_percent': 0.0072, 'trend': 'mild upward momentum led by technology and consumer sectors', 'date': '2024-06-10'}, 'CHINEXT': {'name': 'ChiNext Index', 'latest_close': 2295.67, 'change': 1.25, 'change_percent': 0.0055, 'trend': 'gradual recovery driven by innovation and biotech companies', 'date': '2024-06-10'}, 'STAR50': {'name': 'STAR Market 50 Index', 'latest_close': 1025.78, 'change': -2.14, 'change_percent': -0.0205, 'trend': 'declining due to high valuation concerns in semiconductor stocks', 'date': '2024-06-10'}, 'CSI300': {'name': 'CSI 300 Index', 'latest_close': 3995.25, 'change': -0.85, 'change_percent': -0.0021, 'trend': 'sideways movement with mixed performance in financials and consumer staples', 'date': '2024-06-10'}, 'CSI500': {'name': 'CSI 500 Index', 'latest_close': 5980.45, 'change': 1.02, 'change_percent': 0.0017, 'trend': 'steady gains supported by mid-cap industrial and energy companies', 'date': '2024-06-10'}}
    if indices is not None:
        if not isinstance(indices, list):
            return "Error: 'indices' parameter must be a list of index codes."
        invalid_codes = [code for code in indices if code not in mock_indices_data]
        if invalid_codes:
            return f"Error: Invalid index codes provided: {', '.join(invalid_codes)}"
        selected_data = {code: mock_indices_data[code] for code in indices}
    else:
        selected_data = mock_indices_data
    output_lines = []
    for (code, data) in selected_data.items():
        line = f"{data['name']} ({code}) - Latest Close: {data['latest_close']}, Change: {data['change']} ({data['change_percent'] * 100:.2f}%), Trend: {data['trend']} (as of {data['date']})"
        output_lines.append(line)
    return '\n'.join(output_lines)
if __name__ == '__main__':
    mcp.run(transport='stdio')