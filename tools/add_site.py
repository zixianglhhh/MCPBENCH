from mcp.server.fastmcp import FastMCP
mcp = FastMCP('add_site')

@mcp.tool()
def add_site(domains: list) -> str:
    '''```python
    """
    Create a new PHP website for the specified domain names.

    This function registers a new PHP website using the provided list of domain
    names. It checks for the validity of the domains and ensures that they do
    not already exist. If any domain contains the word "music", the website is
    initialized as an online music review platform with sample content.

    Args:
        domains (list of str): A list of domain names for the new website. Each
            domain must be a non-empty string.

    Returns:
        str: A message indicating the success of the website creation or an
        error message if the input is invalid or if any domain already exists.
    """
```'''
    if not hasattr(add_site, 'mock_db'):
        add_site.mock_db = {'sites': []}
    if not isinstance(domains, list):
        return "Error: 'domains' must be a list of domain names."
    if not domains:
        return 'Error: You must provide at least one domain for the new website.'
    for d in domains:
        if not isinstance(d, str) or not d.strip():
            return f"Error: Invalid domain '{d}'. Domains must be non-empty strings."
    existing_domains = {domain for site in add_site.mock_db['sites'] for domain in site['domains']}
    duplicates = [d for d in domains if d in existing_domains]
    if duplicates:
        return f"Error: The following domain(s) already exist: {', '.join(duplicates)}"
    new_site_id = len(add_site.mock_db['sites']) + 1
    site_entry = {'id': new_site_id, 'domains': domains, 'type': 'PHP', 'description': 'A newly created PHP website.', 'created_at': '2024-06-01 10:00:00', 'posts': [], 'comments': []}
    if any(('music' in d.lower() for d in domains)):
        site_entry['description'] = 'An online music review platform in PHP that features music reviews and recommendations.'
        site_entry['posts'].append({'post_id': 1, 'title': 'Top 10 Albums of the Year', 'content': 'Our music experts review the top 10 albums of this year with in-depth analysis and recommendations.', 'comments': [{'comment_id': 1, 'content': 'Great list! I agree with most of the picks.'}, {'comment_id': 2, 'content': 'I think you missed a few underground gems.'}]})
    add_site.mock_db['sites'].append(site_entry)
    return f"PHP website created successfully for domains: {', '.join(domains)}"
if __name__ == '__main__':
    mcp.run(transport='stdio')