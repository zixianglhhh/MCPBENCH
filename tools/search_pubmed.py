from mcp.server.fastmcp import FastMCP
from typing import Optional
mcp = FastMCP('search_pubmed')

@mcp.tool()
def search_pubmed(query: str, maxResults: Optional[int] = None) -> str:
    '''```python
    """
    Searches PubMed for articles related to specified medical conditions and returns formatted results.

    This function queries PubMed articles based on the provided search query and retrieves a specified
    number of articles. The results include article details and mappings to Experimental Factor Ontology (EFO)
    traits, if applicable.

    Args:
        query (str): The search query to find relevant PubMed articles. Must be a non-empty string.
        maxResults (optional): The maximum number of articles to return. If empty, defaults to 3. Must be a positive integer if provided.

    Returns:
        str: A formatted string containing the details of the PubMed articles found, including titles, authors,
             journals, publication years, abstracts, and related EFO trait mappings. Additionally, the final
             line summarizes all identified EFO IDs across the results. If no articles are found, returns a
             message indicating no results for the given query.
    """
```'''
    mock_pubmed_db = [{'title': 'Biomarkers Predicting Risk of GVHD After Bone Marrow Transplantation', 'authors': ['Smith J', 'Khan A', 'Rodriguez M'], 'journal': 'Journal of Hematology Research', 'year': 2021, 'abstract': 'This study reviews biomarkers associated with predicting graft-versus-host disease (GVHD) risk in bone marrow transplant recipients, based on recent PubMed literature and GWAS trait associations.', 'keywords': ['GVHD', 'biomarkers', 'bone marrow transplantation', 'GWAS']}, {'title': 'GWAS-Identified Genetic Variants Associated with GVHD Susceptibility', 'authors': ['Liu Y', 'Carter P'], 'journal': 'Genetics and Immunology', 'year': 2020, 'abstract': 'A genome-wide association study identifying SNPs linked to increased susceptibility to GVHD in post-transplant patients.', 'keywords': ['GVHD', 'genetic variations', 'GWAS', 'SNPs']}, {'title': 'Hereditary Probabilities of Genetic Diseases: A Comprehensive Review', 'authors': ['Miller D', 'Chen H'], 'journal': 'Genetic Epidemiology', 'year': 2019, 'abstract': 'This paper reviews hereditary probabilities and transmission patterns of various genetic diseases.', 'keywords': ['hereditary', 'genetic diseases', 'probability']}, {'title': 'Genetic Risk Factors for Mental Disorders: Insights from GWAS', 'authors': ['Brown T', 'Singh R'], 'journal': 'Psychiatric Genetics', 'year': 2022, 'abstract': 'A review of genetic variants associated with mental disorders, highlighting findings from large-scale GWAS.', 'keywords': ['mental disorders', 'genetic risk', 'GWAS']}, {'title': "Huntington's Disease: Genetic Mechanisms and Therapeutic Approaches", 'authors': ['Johnson M', 'Williams K', 'Davis L'], 'journal': 'Nature Genetics', 'year': 2023, 'abstract': "Comprehensive analysis of Huntington's disease pathogenesis, focusing on CAG repeat expansion and potential gene therapy interventions for this hereditary neurodegenerative disorder.", 'keywords': ["Huntington's disease", 'hereditary', 'genetic diseases', 'CAG repeat', 'neurodegenerative']}, {'title': 'Cystic Fibrosis: Advances in Gene Therapy and Precision Medicine', 'authors': ['Anderson S', 'Taylor R'], 'journal': 'American Journal of Human Genetics', 'year': 2023, 'abstract': 'Recent breakthroughs in treating cystic fibrosis through gene therapy and CFTR modulator drugs, highlighting the role of genetic testing in personalized treatment approaches.', 'keywords': ['cystic fibrosis', 'hereditary', 'genetic diseases', 'gene therapy', 'CFTR']}, {'title': 'Sickle Cell Disease: Genetic Variants and Population Genetics', 'authors': ['Martinez P', 'Thompson A'], 'journal': 'Blood Genetics', 'year': 2022, 'abstract': 'Population genetics study of sickle cell disease variants across different ethnic groups, examining inheritance patterns and genetic counseling implications.', 'keywords': ['sickle cell disease', 'hereditary', 'genetic diseases', 'population genetics', 'inheritance']}, {'title': 'Schizophrenia: Genome-Wide Association Studies and Polygenic Risk Scores', 'authors': ['Wilson E', 'Clark J'], 'journal': 'Molecular Psychiatry', 'year': 2023, 'abstract': 'Large-scale GWAS analysis identifying novel genetic loci associated with schizophrenia risk, including polygenic risk score development for early detection.', 'keywords': ['schizophrenia', 'mental disorders', 'GWAS', 'polygenic risk', 'genetic loci']}, {'title': 'Bipolar Disorder: Genetic Architecture and Pharmacogenomics', 'authors': ['Lee H', 'Garcia M', 'Patel N'], 'journal': 'Biological Psychiatry', 'year': 2023, 'abstract': 'Comprehensive genetic analysis of bipolar disorder, examining both common and rare variants, with focus on pharmacogenomic implications for treatment selection.', 'keywords': ['bipolar disorder', 'mental disorders', 'pharmacogenomics', 'genetic variants', 'treatment']}, {'title': 'Autism Spectrum Disorders: Genetic Heterogeneity and Family Studies', 'authors': ['Roberts K', 'White S'], 'journal': 'Journal of Autism and Developmental Disorders', 'year': 2022, 'abstract': 'Family-based genetic studies revealing the complex genetic architecture of autism spectrum disorders, including de novo mutations and inherited variants.', 'keywords': ['autism spectrum disorders', 'mental disorders', 'genetic heterogeneity', 'family studies', 'de novo mutations']}]
    if not isinstance(query, str) or not query.strip():
        return "Error: 'query' must be a non-empty string."
    # Normalize and validate maxResults (allow empty / None to default to 3)
    if maxResults in (None, ""):
        max_count = 3
    else:
        try:
            max_count = int(maxResults)
        except (TypeError, ValueError):
            return "Error: 'maxResults' must be a positive integer."
        if max_count <= 0:
            return "Error: 'maxResults' must be a positive integer."
    # Return all articles regardless of the input query, limited by max_count
    results = mock_pubmed_db[:max_count]
    output_lines = []
    for art in results:
        efo_mappings = []
        if 'gvhd' in art['abstract'].lower() or 'graft-versus-host' in art['abstract'].lower():
            efo_mappings.append('EFO_0000305')
        output_lines.append(
            f"Title: {art['title']}\n"
            f"Authors: {', '.join(art['authors'])}\n"
            f"Journal: {art['journal']} ({art['year']})\n"
            f"Abstract: {art['abstract']}\n"
            f"Related EFO Traits: {(', '.join(efo_mappings) if efo_mappings else 'No specific EFO mapping identified')}\n"
        )
    identified_traits = []
    for art in results:
        if 'gvhd' in art['abstract'].lower() or 'graft-versus-host' in art['abstract'].lower():
            if 'EFO_0000305' not in identified_traits:
                identified_traits.append('EFO_0000305')
    summary_line = f"Identified EFO IDs: {', '.join(identified_traits) if identified_traits else 'None'}"
    return '\n'.join(output_lines + [summary_line])
    
if __name__ == '__main__':
    mcp.run(transport='stdio')