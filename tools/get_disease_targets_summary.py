from mcp.server.fastmcp import FastMCP
mcp = FastMCP('get_disease_targets_summary')

@mcp.tool()
def get_disease_targets_summary(diseaseId: str) -> str:
    '''```python
"""
Retrieve all target IDs associated with a specified disease.

This function takes a disease identifier and returns a formatted string containing 
all target IDs linked to the disease. The disease identifier should be a valid string 
representing a known disease.

Args:
    diseaseId (str): A string representing the disease identifier (e.g., 'EFO_0000305').

Returns:
    str: A formatted string listing all target IDs associated with the specified disease.
    If the disease ID is invalid or not found, an error message is returned.
"""
```'''
    mock_disease_targets_db = {'EFO_0000305': {'name': 'Breast Cancer', 'targets': [{'targetId': 'ENSG00000012048', 'symbol': 'BRCA1', 'targetName': 'Breast cancer type 1 susceptibility protein', 'associationScore': 0.95, 'druggability': 'High', 'targetType': 'Protein coding gene'}, {'targetId': 'ENSG00000139618', 'symbol': 'BRCA2', 'targetName': 'Breast cancer type 2 susceptibility protein', 'associationScore': 0.93, 'druggability': 'High', 'targetType': 'Protein coding gene'}, {'targetId': 'ENSG00000141510', 'symbol': 'TP53', 'targetName': 'Tumor protein p53', 'associationScore': 0.91, 'druggability': 'Medium', 'targetType': 'Protein coding gene'}, {'targetId': 'ENSG00000121879', 'symbol': 'ERBB2', 'targetName': 'Receptor tyrosine-protein kinase erbB-2', 'associationScore': 0.89, 'druggability': 'High', 'targetType': 'Protein coding gene'}]}}
    if not diseaseId or not isinstance(diseaseId, str):
        return "Error: 'diseaseId' is required and must be a string."
    if diseaseId not in mock_disease_targets_db:
        return f"Error: Disease ID '{diseaseId}' not found in database."
    disease_data = mock_disease_targets_db[diseaseId]
    target_ids = [target['targetId'] for target in disease_data['targets']]
    return f"Target IDs for {disease_data['name']} ({diseaseId}): {', '.join(target_ids)}"
if __name__ == '__main__':
    mcp.run(transport='stdio')