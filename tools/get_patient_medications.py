from mcp.server.fastmcp import FastMCP
mcp = FastMCP('get_patient_medications')

@mcp.tool()
def get_patient_medications(patientId: str) -> str:
    '''```python
    """
    Retrieve the current medications for a specified patient.

    Args:
        patientId (str): The unique identifier for the patient whose medication
            information is to be retrieved. This should be a non-empty string.

    Returns:
        str: A formatted string listing the patient's current medications, 
        including details such as dosage, indication, and start date. If the 
        patientId is invalid or no records are found, an appropriate error 
        message is returned.
    """
```'''
    mock_medications_db = {'steve_001': [{'medication': 'Lisinopril 10mg', 'dosage': '10 mg once daily', 'indication': 'Hypertension', 'start_date': '2023-08-15'}, {'medication': 'Metformin 500mg', 'dosage': '500 mg twice daily', 'indication': 'Type 2 Diabetes Mellitus', 'start_date': '2022-11-02'}], 'kathy_001': [{'medication': 'Atorvastatin 20mg', 'dosage': '20 mg at bedtime', 'indication': 'Hyperlipidemia', 'start_date': '2023-05-20'}, {'medication': 'Albuterol inhaler', 'dosage': '2 puffs every 4-6 hours as needed', 'indication': 'Asthma', 'start_date': '2021-09-10'}]}
    if patientId is None or not isinstance(patientId, str) or (not patientId.strip()):
        return "Error: A valid 'patientId' string must be provided."
    patientId = patientId.strip().lower()
    if patientId not in mock_medications_db:
        return f"No medication records found for patientId '{patientId}'."
    medications = mock_medications_db[patientId]
    output_lines = [f"Current medications for patient '{patientId}':"]
    for med in medications:
        med_str = f"- {med['medication']}: {med['dosage']} (Indication: {med['indication']}, Started: {med['start_date']})"
        output_lines.append(med_str)
    return '\n'.join(output_lines)
if __name__ == '__main__':
    mcp.run(transport='stdio')