from mcp.server.fastmcp import FastMCP
mcp = FastMCP('CafChem_ADME_calc_adme')

@mcp.tool()
def CafChem_ADME_calc_adme(smile: str) -> str:
    '''```python
"""
Calculate the ADME properties of a molecule from a SMILES string.

This function evaluates the Absorption, Distribution, Metabolism, and Excretion (ADME) properties of a given molecule, which are crucial for understanding how a drug is transported and processed by the body. The calculated properties adhere to Lipinski's Rule of Five, which is a guideline for determining drug-likeness.

Args:
    smile (str): A non-empty SMILES string representing the molecular structure of the compound.

Returns:
    tuple: A tuple containing:
        - str: A text string summarizing the ADME properties, including:
            - Qualitative Estimate of Drug-likeness (QED)
            - Molecular Weight (MW) in g/mol
            - Distribution Coefficient (aLogP)
            - Number of Hydrogen Bond Donors (HBD)
            - Number of Hydrogen Bond Acceptors (HBA)
            - Polar Surface Area (PSA) in Å²
            - Number of Rotatable Bonds
            - Number of Aromatic Rings
            - Number of Undesirable Moieties
        - str: An image representation of the molecule.
"""
```'''
    mock_adme_db = {'Cn1cnc2c1c(=O)n(c(=O)n2C)': {'QED': 0.78, 'MW': 194.19, 'aLogP': -0.07, 'HBD': 0, 'HBA': 4, 'PSA': 61.82, 'RotB': 0, 'AromaticRings': 2, 'UndesirableMoieties': 0, 'image': '<image of caffeine molecule>'}, 'CC(=O)OC1=CC=CC=C1C(=O)O': {'QED': 0.68, 'MW': 180.16, 'aLogP': 1.19, 'HBD': 1, 'HBA': 4, 'PSA': 63.6, 'RotB': 3, 'AromaticRings': 1, 'UndesirableMoieties': 0, 'image': '<image of aspirin molecule>'}, 'CC1=CC=C(C=C1)NC2=NC=NC3=C2C=CC(=C3)C(=O)NC4=CC=CC=C4': {'QED': 0.54, 'MW': 493.6, 'aLogP': 3.25, 'HBD': 2, 'HBA': 8, 'PSA': 86.28, 'RotB': 7, 'AromaticRings': 3, 'UndesirableMoieties': 1, 'image': '<image of imatinib molecule>'}, 'O=C(NC1=CC=CC=C1)C2=NC=NC=N2': {'QED': 0.72, 'MW': 201.22, 'aLogP': 1.45, 'HBD': 1, 'HBA': 5, 'PSA': 78.12, 'RotB': 2, 'AromaticRings': 2, 'UndesirableMoieties': 0, 'image': '<image of O=C(NC1=CC=CC=C1)C2=NC=NC=N2 molecule>'}}
    if not isinstance(smile, str) or not smile.strip():
        raise ValueError('Invalid SMILES string: must be a non-empty string.')
    smile = smile.strip()
    if smile in mock_adme_db:
        props = mock_adme_db[smile]
    else:
        props = {'QED': round(0.5 + 0.3 * (hash(smile) % 100) / 100, 2), 'MW': round(150 + hash(smile) % 400, 2), 'aLogP': round(-1 + hash(smile) % 70 / 10, 2), 'HBD': hash(smile) % 5, 'HBA': hash(smile[::-1]) % 10, 'PSA': round(20 + hash(smile) % 140, 2), 'RotB': hash(smile) % 10, 'AromaticRings': hash(smile) % 5, 'UndesirableMoieties': hash(smile[::-1]) % 3, 'image': f'<image of molecule for SMILES: {smile}>'}
    adme_text = f"QED: {props['QED']}, Molecular Weight: {props['MW']} g/mol, aLogP: {props['aLogP']}, H-bond Donors: {props['HBD']}, H-bond Acceptors: {props['HBA']}, Polar Surface Area: {props['PSA']} Å², Rotatable Bonds: {props['RotB']}, Aromatic Rings: {props['AromaticRings']}, Undesirable Moieties: {props['UndesirableMoieties']}."
    return (adme_text, props['image'])
if __name__ == '__main__':
    mcp.run(transport='stdio')