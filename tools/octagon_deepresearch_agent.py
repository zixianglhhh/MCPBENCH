from mcp.server.fastmcp import FastMCP
from typing import List
mcp = FastMCP('octagon_deepresearch_agent')

@mcp.tool()
def octagon_deepresearch_agent(companies: List[str], fields: List[str]) -> str:
    '''```python
    """
    Conduct comprehensive research on a list of companies to enhance their profiles with detailed information. 
    This function enriches company profiles by providing additional context such as descriptions, leadership, 
    funding, partnerships, and recent news. It complements the octagon-companies-agent by offering more nuanced 
    and qualitative insights.

    Args:
        companies (List[str]): A non-empty list of company names or IDs for which detailed research is to be performed.
            All company names should be provided in lowercase in alphabetical orderß.
        fields (List[str]): An optional list of specific fields to include in the research results. Each field should 
            be a string representing a key in the company profile. All field names should be in lowercase. List should be given in alphabetical order.
            Available fields: 'name', 'domain', 'revenue_growth', 'description', 'logo_url', 'hq_location', 
            'country', 'linkedin_url', 'contact_info', 'strategic_focus'.

    Returns:
        str: A JSON-formatted string containing the enriched profiles of the specified companies. If specific fields 
        are provided, only those fields will be included in the output. If a company cannot be found, an error message 
        will be included in its place.
    """
```'''
    if not isinstance(companies, list) or not companies:
        raise ValueError("Parameter 'companies' must be a non-empty list of company names or IDs.")
    if fields is not None and (not isinstance(fields, list) or not all((isinstance(f, str) for f in fields))):
        raise ValueError("Parameter 'fields' must be a list of strings if provided.")
    mock_company_profiles = {'ibm': {'name': 'IBM', 'domain': 'ibm.com', 'revenue_growth': '1.5%', 'description': 'IBM is a global technology and consulting company offering infrastructure, software, and services.', 'logo_url': 'https://logo.clearbit.com/ibm.com', 'hq_location': 'Armonk, New York', 'country': 'United States', 'linkedin_url': 'https://www.linkedin.com/company/ibm', 'contact_info': {'website': 'https://www.ibm.com', 'phone': '+1-914-499-1900', 'email': 'info@ibm.com', 'address': 'One New Orchard Road, Armonk, NY 10504, USA'}, 'strategic_focus': 'Cloud computing, AI, hybrid cloud solutions, and quantum computing.'}, 'microsoft': {'name': 'Microsoft', 'domain': 'microsoft.com', 'revenue_growth': '14.0%', 'description': 'Microsoft develops, licenses, and supports a range of software products, services, and devices.', 'logo_url': 'https://logo.clearbit.com/microsoft.com', 'hq_location': 'Redmond, Washington', 'country': 'United States', 'linkedin_url': 'https://www.linkedin.com/company/microsoft', 'contact_info': {'website': 'https://www.microsoft.com', 'phone': '+1-425-882-8080', 'email': 'info@microsoft.com', 'address': 'One Microsoft Way, Redmond, WA 98052, USA'}, 'strategic_focus': 'Cloud services, AI integration, productivity software, and gaming.'}, 'google': {'name': 'Google', 'domain': 'google.com', 'revenue_growth': '8.0%', 'description': 'Google develops and provides Internet-related services and products including search, cloud computing, software and hardware.', 'logo_url': 'https://logo.clearbit.com/google.com', 'hq_location': 'Mountain View, California', 'country': 'United States', 'linkedin_url': 'https://www.linkedin.com/company/google', 'contact_info': {'website': 'https://www.google.com', 'phone': '+1-650-253-0000', 'email': 'press@google.com', 'address': '1600 Amphitheatre Parkway, Mountain View, CA 94043, USA'}, 'strategic_focus': 'Search, advertising, AI research, cloud computing, and hardware.'}, 'oracle': {'name': 'Oracle', 'domain': 'oracle.com', 'revenue_growth': '5.0%', 'description': 'Oracle offers integrated cloud applications and platform services.', 'logo_url': 'https://logo.clearbit.com/oracle.com', 'hq_location': 'Austin, Texas', 'country': 'United States', 'linkedin_url': 'https://www.linkedin.com/company/oracle', 'contact_info': {'website': 'https://www.oracle.com', 'phone': '+1-512-678-7000', 'email': 'info@oracle.com', 'address': '2300 Oracle Way, Austin, TX 78741, USA'}, 'strategic_focus': 'Database management, cloud applications, enterprise software, and AI integration.'}, 'accenture': {'name': 'Accenture', 'domain': 'accenture.com', 'revenue_growth': '3.5%', 'description': 'Accenture provides consulting, technology, and outsourcing services worldwide.', 'logo_url': 'https://logo.clearbit.com/accenture.com', 'hq_location': 'Dublin', 'country': 'Ireland', 'linkedin_url': 'https://www.linkedin.com/company/accenture', 'contact_info': {'website': 'https://www.accenture.com', 'phone': '+353-1-646-2000', 'email': 'info@accenture.com', 'address': '1 Grand Canal Square, Grand Canal Harbour, Dublin 2, Ireland'}, 'strategic_focus': 'Digital transformation, AI consulting, cloud migration, and automation services.'}, 'sap': {'name': 'SAP', 'domain': 'sap.com', 'revenue_growth': '2.5%', 'description': 'SAP is a market leader in enterprise application software, helping companies run better.', 'logo_url': 'https://logo.clearbit.com/sap.com', 'hq_location': 'Walldorf', 'country': 'Germany', 'linkedin_url': 'https://www.linkedin.com/company/sap', 'contact_info': {'website': 'https://www.sap.com', 'phone': '+49-622-777-0000', 'email': 'info@sap.com', 'address': 'Dietmar-Hopp-Allee 16, 69190 Walldorf, Germany'}, 'strategic_focus': 'Enterprise software, cloud computing, AI integration, and sustainability solutions.'}}
    result = {}
    for company in companies:
        profile = mock_company_profiles.get(company)
        if not profile:
            result[company] = {'error': 'No deep research data available for this company.'}
            continue
        if fields:
            filtered_profile = {}
            for field in fields:
                if field in profile:
                    filtered_profile[field] = profile[field]
            result[company] = filtered_profile
        else:
            result[company] = profile
    import json
    return json.dumps(result, indent=2)
if __name__ == '__main__':
    mcp.run(transport='stdio')