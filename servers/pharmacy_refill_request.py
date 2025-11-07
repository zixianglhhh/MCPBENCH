from mcp.server.fastmcp import FastMCP
from typing import Literal
mcp = FastMCP('pharmacy_refill_request')

@mcp.tool()
def pharmacy_refill_request(prescription_id: str, patient_dob: str, pharmacy_branch: Literal['DOWNTOWN', 'NORTH', 'EAST', 'SOUTH', 'WEST']) -> str:
    '''"""
Initiate a refill request for a prescription at a selected pharmacy branch.

The request is validated against the mock refill registry. Only active prescriptions
with remaining refills can be processed. The `patient_dob` must match the record on
file in `YYYY-MM-DD` format. The tool returns a pickup estimate once the request is
accepted.

Args:
    prescription_id (str): Unique prescription number printed on the label.
    patient_dob (str): Birth date in `YYYY-MM-DD` format for verification.
    pharmacy_branch (Literal['DOWNTOWN', 'NORTH', 'EAST', 'SOUTH', 'WEST']): Desired pickup branch.

Returns:
    str: Confirmation message with the ready time or a detailed rejection reason.
"""'''
    registry = {
        'RX-204811': {'dob': '1987-05-19', 'refills_left': 2, 'medication': 'Lisinopril 10mg'},
        'RX-305722': {'dob': '1994-11-03', 'refills_left': 0, 'medication': 'Metformin 500mg'},
        'RX-118932': {'dob': '1979-02-24', 'refills_left': 1, 'medication': 'Atorvastatin 20mg'},
        'RX-990143': {'dob': '2001-07-12', 'refills_left': 3, 'medication': 'Albuterol Inhaler'},
    }
    if not prescription_id:
        return "Error: 'prescription_id' is required."
    if not patient_dob:
        return "Error: 'patient_dob' is required."
    if pharmacy_branch not in ['DOWNTOWN', 'NORTH', 'EAST', 'SOUTH', 'WEST']:
        return "Error: Invalid pharmacy branch."
    record = registry.get(prescription_id)
    if not record:
        return f"Error: Prescription '{prescription_id}' not found."
    if patient_dob != record['dob']:
        return "Error: Date of birth does not match the prescription record."
    if record['refills_left'] <= 0:
        return "Error: No refills remaining. Contact your provider."
    ready_in_hours = 3 if pharmacy_branch in ['DOWNTOWN', 'NORTH'] else 6
    return (
        "Refill request accepted!\n"
        f"Medication: {record['medication']}\n"
        f"Refills Remaining After Pickup: {record['refills_left'] - 1}\n"
        f"Pickup Branch: {pharmacy_branch}\n"
        f"Ready In: {ready_in_hours} hour(s)"
    )
if __name__ == '__main__':
    mcp.run(transport='stdio')
