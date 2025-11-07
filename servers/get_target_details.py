from mcp.server.fastmcp import FastMCP
mcp = FastMCP('get_target_details')

@mcp.tool()
def get_target_details(target_ids: list) -> str:
    '''```python
    """
    Retrieve detailed information for a list of target IDs.

    This function accepts a list of target IDs and returns comprehensive 
    information for each target, including symbol, name, associated diseases, 
    biological function, expression profile, druggability, and candidate compounds.

    Args:
        target_ids (list of str): A non-empty list of target IDs for which 
            details are to be retrieved. Each target ID must be a non-empty string.
            only accept Ensembl gene ID

    Returns:
        str: A formatted string containing detailed information for each target ID 
        provided. If an error occurs, such as an invalid target ID or a target 
        ID not found, an appropriate error message is included in the output.
    """
```'''
    mock_target_db = {'ENSG00000141510': {'symbol': 'TP53', 'name': 'Tumor protein p53', 'associated_diseases': [{'name': 'Li-Fraumeni syndrome', 'evidence_score': 0.99}, {'name': 'Ovarian cancer', 'evidence_score': 0.85}], 'biological_function': "TP53 is a tumor suppressor gene that encodes a transcription factor involved in preventing cancer formation. It regulates the cell cycle and functions as a tumor suppressor, hence referred to as the 'guardian of the genome'.", 'expression_profile': {'tissues': ['ubiquitous'], 'expression_level': 'Widely expressed in all tissues'}, 'druggability': {'small_molecule': False, 'antibody': False, 'known_drugs': [], 'druggability_score': 0.4}, 'candidate_compounds': [{'name': 'TP53_path_mock1', 'smiles': 'C1=CC(=O)NC(=O)N1'}, {'name': 'TP53_path_mock2', 'smiles': 'CC(C)C1=NC=NC(=N1)N'}]}, 'ENSG00000012048': {'symbol': 'BRCA1', 'name': 'Breast cancer type 1 susceptibility protein', 'associated_diseases': [{'name': 'Breast cancer', 'evidence_score': 0.95}, {'name': 'Ovarian cancer', 'evidence_score': 0.9}], 'biological_function': 'BRCA1 is a tumor suppressor gene that plays a critical role in DNA repair and maintenance of genomic stability. It is involved in homologous recombination and double-strand break repair.', 'expression_profile': {'tissues': ['breast', 'ovary', 'ubiquitous'], 'expression_level': 'High in breast and ovarian tissues'}, 'druggability': {'small_molecule': True, 'antibody': True, 'known_drugs': ['Olaparib', 'Rucaparib'], 'druggability_score': 0.85}, 'candidate_compounds': [{'name': 'BRCA_path_mock2', 'smiles': 'O=C(NC1=CC=CC=C1)C2=NC=NC=N2'}]}, 'ENSG00000139618': {'symbol': 'BRCA2', 'name': 'Breast cancer type 2 susceptibility protein', 'associated_diseases': [{'name': 'Breast cancer', 'evidence_score': 0.93}, {'name': 'Ovarian cancer', 'evidence_score': 0.88}], 'biological_function': 'BRCA2 is a tumor suppressor gene involved in DNA repair and homologous recombination. It works in conjunction with BRCA1 to maintain genomic stability and prevent tumor formation.', 'expression_profile': {'tissues': ['breast', 'ovary', 'testis'], 'expression_level': 'High in reproductive tissues'}, 'druggability': {'small_molecule': True, 'antibody': True, 'known_drugs': ['Olaparib', 'Rucaparib', 'Talazoparib'], 'druggability_score': 0.87}, 'candidate_compounds': [{'name': 'BRCA_path_mock1', 'smiles': 'COC1=CC=CC=C1C(=O)N2C=NC3=CC=CC=C23'}]}, 'ENSG00000121879': {'symbol': 'ERBB2', 'name': 'Receptor tyrosine-protein kinase erbB-2', 'associated_diseases': [{'name': 'Breast cancer', 'evidence_score': 0.89}, {'name': 'Gastric cancer', 'evidence_score': 0.75}], 'biological_function': 'ERBB2 (HER2) is a receptor tyrosine kinase that plays a crucial role in cell growth, differentiation, and survival. It is frequently amplified in breast cancer.', 'expression_profile': {'tissues': ['breast', 'stomach', 'heart'], 'expression_level': 'High in epithelial tissues'}, 'druggability': {'small_molecule': True, 'antibody': True, 'known_drugs': ['Trastuzumab', 'Lapatinib', 'Pertuzumab'], 'druggability_score': 0.92}, 'candidate_compounds': [{'name': 'HER2_tki_mock1', 'smiles': 'N=C(N)N1C=NC2=CC=CC=C12'}, {'name': 'HER2_tki_mock2', 'smiles': 'CCN1C(=O)NC(=O)N(C)C1=O'}]}}
    if not isinstance(target_ids, list) or not target_ids:
        return "Error: 'target_ids' must be a non-empty list of target IDs."
    all_results = []
    for target_id in target_ids:
        if not isinstance(target_id, str) or not target_id.strip():
            all_results.append(f"Error: Invalid target ID '{target_id}' - must be a non-empty string.")
            continue
        target_info = mock_target_db.get(target_id)
        if not target_info:
            all_results.append(f"Error: No target found for Ensembl ID '{target_id}'.")
            continue
        target_output = [f'Target ID: {target_id}', f"Symbol: {target_info['symbol']}", f"Name: {target_info['name']}", 'Associated Diseases:']
        for disease in target_info['associated_diseases']:
            target_output.append(f"  - {disease['name']} (Evidence score: {disease['evidence_score']})")
        target_output.append(f"Biological Function: {target_info['biological_function']}")
        target_output.append(f"Expression Profile: High expression in {', '.join(target_info['expression_profile']['tissues'])} ({target_info['expression_profile']['expression_level']})")
        target_output.append('Druggability:')
        target_output.append(f"  - Small Molecule: {target_info['druggability']['small_molecule']}")
        target_output.append(f"  - Antibody: {target_info['druggability']['antibody']}")
        target_output.append(f"  - Known Drugs: {(', '.join(target_info['druggability']['known_drugs']) if target_info['druggability']['known_drugs'] else 'None')}")
        target_output.append(f"  - Druggability Score: {target_info['druggability']['druggability_score']}")
        if 'candidate_compounds' in target_info and target_info['candidate_compounds']:
            target_output.append('Candidate Compounds:')
            for compound in target_info['candidate_compounds']:
                target_output.append(f"  - {compound['name']}: {compound['smiles']}")
        else:
            target_output.append('Candidate Compounds: None available')
        all_results.append('\n'.join(target_output))
    return '\n\n' + '=' * 80 + '\n\n'.join(all_results)
if __name__ == '__main__':
    mcp.run(transport='stdio')