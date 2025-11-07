from mcp.server.fastmcp import FastMCP
mcp = FastMCP('octagon_companies_agent')

@mcp.tool()
def octagon_companies_agent(seed_company: str, limit: int) -> str:
    '''```python
    """
    Retrieves a list of companies similar to a given reference company, limited to a specified count.

    This function identifies companies within the same business domain or industry as the provided
    seed company. It returns a curated list of potential competitors, partners, or similar businesses,
    which can be useful for competitive analysis, partnership identification, and market research.

    Args:
        seed_company (str): The name or domain of the reference company for which similar companies are sought.
            Must be a non-empty string.
        limit (int): The maximum number of similar companies to return. Must be a positive integer greater than 0.

    Returns:
        str: A JSON-formatted string containing an array of similar company names, limited to the specified count.

    Example:
        octagon_companies_agent("IBM", 3) -> '["Microsoft", "Oracle", "Accenture"]'
    """
```'''
    mock_companies_db = {'IBM': ['Microsoft', 'Oracle', 'Accenture', 'Google', 'SAP']}
    if not isinstance(seed_company, str) or not seed_company.strip():
        return "Error: 'seed_company' must be a non-empty string representing a domain or company name."
    if not isinstance(limit, int) or limit <= 0:
        return "Error: 'limit' must be a positive integer greater than 0."
    seed_company_lower = seed_company.lower().strip()
    if seed_company_lower != 'ibm':
        return f"Error: Seed company '{seed_company}' not found in the database."
    all_similar_companies = mock_companies_db['IBM']
    limited_companies = all_similar_companies[:limit]
    import json
    return json.dumps(limited_companies, indent=2)
if __name__ == '__main__':
    mcp.run(transport='stdio')