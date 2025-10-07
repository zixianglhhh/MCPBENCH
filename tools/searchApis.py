from mcp.server.fastmcp import FastMCP
'\nsearchApis Server\n-----------------\nA minimal MCP server exposing a single tool: `searchApis`.\n\nPurpose:\n- Given a *label keyword* (e.g., "object detection", "earthquake", "translation"),\n  return the APIs grouped under that label.\n- label keyword is \n- If the provided keyword isn\'t an exact label, the tool performs a fallback partial\n  match against labels and (if needed) API names.\n\n\nReturn format:\n- If exactly one label is matched: "<label>: api1, api2, ..."\n- If multiple labels are matched: one line per label, each line in the same format.\n- If none matched: "No APIs found for keyword \'<keyword>\'."\n\nNotes:\n- Matching is case-insensitive and trims whitespace.\n'
mcp = FastMCP('searchApis')

@mcp.tool()
def searchApis(keyword: str) -> str:
    '''```python
    """
    Searches for APIs based on a given label keyword, with a case-insensitive approach.

    The search prioritizes:
      1) Exact label matches
      2) Partial label matches (as substrings)
      3) Partial API-name matches (as substrings)

    The function returns a formatted string with the results:
      - For a single label match: "<label>: api1, api2, ..."
      - For multiple label matches: Each label and its APIs on a new line in the format "<label>: api1, api2, ..."
      - If no matches are found: "No APIs found for keyword '<keyword>'."

    Args:
        keyword (str): The label keyword to search for. Must be a non-empty string.

    Returns:
        str: A formatted string of matched APIs or an error message if no matches are found.
    """
```'''
    if not isinstance(keyword, str) or not keyword.strip():
        return "Error: 'keyword' must be a non-empty string."
    q = keyword.strip().lower()
    mock_api_db = {'object detection': ['Image Object Detection API', 'Vision Detect Pro API'], 'image recognition': ['Image Object Detection API', 'Vision Detect Pro API', 'OCR Text Extract API'], 'earthquake': ['City Earthquake Data API', 'USGS Earthquake Feed API (Mock)'], 'translation': ['Microsoft Translator Text API', 'Simple & Elegant Translation Service API'], 'language correction': ['LanguageTool API', 'Grammarify Proofread API (Mock)']}
    api_to_labels = {}
    for (label, apis) in mock_api_db.items():
        for api in apis:
            api_to_labels.setdefault(api, set()).add(label)
    exact_hits = []
    for label in db.keys():
        if q == label.lower():
            exact_hits.append(label)
    if exact_hits:
        ordered = [lbl for lbl in mock_api_db.keys() if lbl in exact_hits]
        lines = [f"{lbl}: {', '.join(mock_api_db[lbl])}" for lbl in ordered]
        return '\n'.join(lines)
    partial_label_hits = []
    for label in mock_api_db.keys():
        if q in label.lower():
            partial_label_hits.append(label)
    if partial_label_hits:
        ordered = [lbl for lbl in mock_api_db.keys() if lbl in partial_label_hits]
        lines = [f"{lbl}: {', '.join(mock_api_db[lbl])}" for lbl in ordered]
        return '\n'.join(lines)
    candidate_labels = []
    for api_name in api_to_labels.keys():
        if q in api_name.lower():
            candidate_labels.extend(list(api_to_labels[api_name]))
    seen = set()
    ordered_candidates = []
    for lbl in mock_api_db.keys():
        if lbl in candidate_labels and lbl not in seen:
            seen.add(lbl)
            ordered_candidates.append(lbl)
    if ordered_candidates:
        lines = [f"{lbl}: {', '.join(db[lbl])}" for lbl in ordered_candidates]
        return '\n'.join(lines)
    return f"No APIs found for keyword '{keyword.strip()}'."
if __name__ == '__main__':
    mcp.run(transport='stdio')