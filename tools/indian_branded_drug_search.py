from mcp.server.fastmcp import FastMCP

mcp = FastMCP("indian_branded_drug_search")

@mcp.tool()
def indian_branded_drug_search(drug_name: str, generic_composition: str, drug_form: str, volume: str) -> str:
    '''```python
    """
    Lookup branded drugs in India from a mock dataset and return detailed metadata.

    This tool demonstrates a structured search over an in-memory list of drug entries, matching on drug name,
    generic composition, form, and volume. When an exact match is found, comprehensive metadata is returned.

    Args:
        drug name (str): Branded drug name to search for (exact match, case-insensitive).
        generic composition (str): The generic composition (exact match, case-insensitive).
        drug form (str): The dosage form (e.g., Tablet, Ophthalmic Solution).
        volume (str): The strength/volume (e.g., "500mg", "5ml").

    Returns:
        str: A formatted block containing drug metadata (manufacturer, usage instructions, precautions), or an
        error message if no match is found or if required parameters are missing.
    """
    ```'''
    # Mock database of drugs
    mock_drug_database = [
        {
            "drug_name": "Saikongqing",
            "generic_composition": "Brimonidine",
            "drug_form": "Ophthalmic Solution",
            "volume": "5ml",
            "manufacturer": "XYZ Pharma Pvt Ltd",
            "usage_instructions": "Instill one drop in the affected eye(s) twice daily.",
            "precautions": "Avoid touching the dropper tip to any surface to prevent contamination. Do not use if the solution changes color."
        },
        {
            "drug_name": "Paracet",
            "generic_composition": "Paracetamol",
            "drug_form": "Tablet",
            "volume": "500mg",
            "manufacturer": "ABC Pharmaceuticals",
            "usage_instructions": "Take one tablet every 4 to 6 hours as needed.",
            "precautions": "Do not exceed 8 tablets in 24 hours. Consult a doctor if symptoms persist."
        }
    ]

    # Validate inputs
    if not drug_name or not generic_composition or not drug_form or not volume:
        return "Error: All parameters (drug name, generic composition, drug form, volume) must be provided."

    # Search the mock database for a matching drug
    for drug in mock_drug_database:
        if (drug["drug_name"].lower() == drug_name.lower() and
                drug["generic_composition"].lower() == generic_composition.lower() and
                drug["drug_form"].lower() == drug_form.lower() and
                drug["volume"].lower() == volume.lower()):
            # Return comprehensive metadata about the drug
            response = (
                f"Drug Name: {drug['drug_name']}\n"
                f"Generic Composition: {drug['generic_composition']}\n"
                f"Form: {drug['drug_form']}\n"
                f"Volume: {drug['volume']}\n"
                f"Manufacturer: {drug['manufacturer']}\n"
                f"Usage Instructions: {drug['usage_instructions']}\n"
                f"Precautions: {drug['precautions']}"
            )
            return response

    # If no match is found
    return "Error: No matching drug found in the database."

if __name__ == "__main__":
    mcp.run(transport='stdio')
