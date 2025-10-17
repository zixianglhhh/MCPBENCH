from mcp.server.fastmcp import FastMCP
mcp = FastMCP('UIUX_Expert')

@mcp.tool()
def UIUX_Expert(user_personas: str, interaction_modes: str, design_principles: str, prototyping_tools: str, usability_testing: str, output_artifacts: str) -> str:
    '''```python
    """
    Focuses on user interface and experience design by evaluating and applying 
    specified design parameters to create tailored UI/UX solutions.

    Args:
        user_personas (str): A description of the target audience, including 
            demographic and behavioral characteristics.
        interaction_modes (str): The methods through which users will interact 
            with the system, such as voice commands or text chat.
        design_principles (str): The foundational guidelines for design, 
            including aspects like accessibility and visual aesthetics.
        prototyping_tools (str): The software tools used for creating design 
            prototypes, such as Figma or Adobe XD.
        usability_testing (str): The strategies employed to test the design's 
            effectiveness and user satisfaction, including A/B testing and 
            heuristic evaluations.
        output_artifacts (str): The final deliverables of the design process, 
            such as prototypes and test reports.

    Returns:
        str: A message indicating the completion status of the UI/UX design 
        process, including a summary of the applied parameters and readiness 
        for stakeholder review.
    """
```'''
    mock_db = {'Design a new interaction interface for the chating robot.': {'user_personas': 'Young adults (18-35) who frequently use messaging apps, prefer quick and intuitive UI, comfortable with emojis and GIFs.', 'interaction_modes': 'Voice commands, text chat, gesture recognition.', 'design_principles': 'Minimalist design, high contrast for readability, responsive layout, accessibility compliance (WCAG 2.1).', 'prototyping_tools': 'Figma, Adobe XD, InVision.', 'usability_testing': 'A/B testing with 50 users, heuristic evaluation, think-aloud protocol.', 'output_artifacts': 'Interactive prototype, persona documentation, usability test report.'}, 'Research and analyze the market demand for caregiver robots, design a robot that can help people complete daily household activities, including market research, demand analysis, design, implementation, testing, optimization, and interactive interface.': {'user_personas': 'Elderly individuals living alone, people with mobility impairments, caregivers needing assistance.', 'interaction_modes': 'Touchscreen interface, voice commands, mobile app control.', 'design_principles': 'User-friendly navigation, large and clear icons, empathetic visual tone, multilingual support.', 'prototyping_tools': 'Sketch, Figma, Axure RP.', 'usability_testing': 'Home-based user trials, task completion time measurement, satisfaction surveys.', 'output_artifacts': 'High-fidelity mockups, interaction flow diagrams, accessibility compliance checklist.'}}
    if not all((isinstance(param, str) and param.strip() for param in [user_personas, interaction_modes, design_principles, prototyping_tools, usability_testing, output_artifacts])):
        raise ValueError('All parameters must be non-empty strings.')
    matched_scenario = None
    for (scenario, data) in mock_db.items():
        if data['user_personas'] == user_personas.strip() and data['interaction_modes'] == interaction_modes.strip():
            matched_scenario = scenario
            break
    if not matched_scenario:
        return 'UI/UX design process completed successfully with provided parameters.'
    result = f"UI/UX design for scenario: '{matched_scenario}' completed.\nUser Personas: {user_personas}\nInteraction Modes: {interaction_modes}\nDesign Principles: {design_principles}\nPrototyping Tools: {prototyping_tools}\nUsability Testing: {usability_testing}\nOutput Artifacts: {output_artifacts}\nStatus: Design ready for stakeholder review."
    return result
if __name__ == '__main__':
    mcp.run(transport='stdio')