from mcp.server.fastmcp import FastMCP
mcp = FastMCP('get_trait_associations')

@mcp.tool()
def get_trait_associations(efoId: str) -> str:
    '''```python
    """
    Retrieves genome-wide association study (GWAS) results that link a specific trait, phenotype, 
    or disease, identified by its Experimental Factor Ontology (EFO) ID, to associated genetic 
    variants, loci, and related metadata. The function queries curated resources such as the GWAS 
    Catalog to provide structured information on variant–trait associations. This includes variant 
    identifiers (e.g., rsIDs), mapped genes, effect sizes (odds ratio or beta), p-values, study 
    metadata, sample ancestry, and publication references. The results can be utilized to explore 
    potential genetic biomarkers, validate findings against published studies, and support 
    downstream analyses such as risk prediction, trait correlation, or candidate gene prioritization. 
    The function focuses exclusively on returning association data and can integrate results from 
    PubMed literature searches for comprehensive biomarker analysis.

    Args:
        efoId (str): The Experimental Factor Ontology (EFO) ID representing the specific trait, 
            phenotype, or disease for which GWAS associations are to be retrieved. Must be a 
            non-empty string.

    Returns:
        str: A formatted string containing the GWAS associations for the specified trait, including 
        details such as variant identifiers, mapped genes, effect sizes, p-values, study metadata, 
        sample ancestry, and publication references.
    """
```'''
    mock_gwas_data = {'EFO_0000305': {'trait': 'Graft-versus-host disease', 'associations': [{'variant_id': 'rs123456', 'mapped_gene': 'IL10', 'effect_size': {'odds_ratio': 1.85, 'ci_95': [1.5, 2.2]}, 'p_value': 4.2e-08, 'study': 'Genome-wide association study of GVHD in bone marrow transplant recipients', 'sample_ancestry': 'European', 'publication': {'pmid': '31234567', 'journal': 'Blood', 'year': 2020}}, {'variant_id': 'rs987654', 'mapped_gene': 'TNF', 'effect_size': {'odds_ratio': 1.42, 'ci_95': [1.2, 1.65]}, 'p_value': 2.1e-07, 'study': 'Genetic risk loci for GVHD identified in multi-center cohort', 'sample_ancestry': 'Asian', 'publication': {'pmid': '29876543', 'journal': 'Nature Genetics', 'year': 2019}}]}, 'EFO_0000692': {'trait': 'Schizophrenia', 'associations': [{'variant_id': 'rs6994992', 'mapped_gene': 'NRG1', 'effect_size': {'odds_ratio': 1.15, 'ci_95': [1.1, 1.2]}, 'p_value': 5.6e-10, 'study': 'GWAS meta-analysis of schizophrenia across diverse populations', 'sample_ancestry': 'Mixed (European, Asian)', 'publication': {'pmid': '25056061', 'journal': 'Nature', 'year': 2014}}, {'variant_id': 'rs1625579', 'mapped_gene': 'MIR137', 'effect_size': {'odds_ratio': 1.25, 'ci_95': [1.18, 1.32]}, 'p_value': 3e-12, 'study': 'Common variants at MIR137 influence risk of schizophrenia', 'sample_ancestry': 'European', 'publication': {'pmid': '21926974', 'journal': 'Nature Genetics', 'year': 2012}}]}, 'EFO_0000270': {'trait': 'Cystic fibrosis', 'associations': [{'variant_id': 'rs113993960', 'mapped_gene': 'CFTR', 'effect_size': {'beta': -2.5, 'unit': 'FEV1 % predicted'}, 'p_value': 1.2e-20, 'study': 'CFTR variants and lung function decline in cystic fibrosis', 'sample_ancestry': 'European', 'publication': {'pmid': '22085960', 'journal': 'American Journal of Respiratory and Critical Care Medicine', 'year': 2011}}]}}
    if not isinstance(efoId, str) or not efoId.strip():
        return "Error: 'efoId' must be a non-empty string."
    if efoId not in mock_gwas_data:
        return f"No GWAS associations found for EFO ID '{efoId}'."
    trait_data = mock_gwas_data[efoId]
    output_lines = [f"GWAS Associations for trait '{trait_data['trait']}' (EFO ID: {efoId}):"]
    for assoc in trait_data['associations']:
        line = f"- Variant: {assoc['variant_id']} | Gene: {assoc['mapped_gene']} | Effect: {assoc['effect_size']} | p-value: {assoc['p_value']:.2e} | Study: {assoc['study']} | Ancestry: {assoc['sample_ancestry']} | Publication: PMID {assoc['publication']['pmid']} ({assoc['publication']['journal']}, {assoc['publication']['year']})"
        output_lines.append(line)
    output_lines.append(f'\nBiomarker Assessment Summary:')
    output_lines.append('- Literature supports genetic biomarkers for GVHD risk prediction')
    output_lines.append('- Combined PubMed and GWAS data show consistent biomarker associations')
    output_lines.append('- These genetic variants can be used for risk stratification in clinical settings')
    return '\n'.join(output_lines)
if __name__ == '__main__':
    mcp.run(transport='stdio')