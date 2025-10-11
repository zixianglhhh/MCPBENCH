from mcp.server.fastmcp import FastMCP
mcp = FastMCP('system_architecture_designer')

@mcp.tool()
def system_architecture_designer(system_design: str, technology_stack: str, hardware_requirements: str, interaction_interface: str, test_optimization_plan: str) -> str:
    '''```python
    """
    Designs high-level system architecture and plans technology strategies for various projects, including robots, websites, and simulation systems. Focuses on defining system structure, selecting technology stacks, and determining hardware/software requirements. Provides guidance for interaction design and optimization when necessary. In tasks involving multiple tools, this function exclusively manages architecture and design aspects, delegating other responsibilities to appropriate tools.
    Unable to achieve geographically related system design.
    Args:
        system_design (str): A description of the desired system architecture, detailing the structural components and their interactions.
        technology_stack (str): A specification of the technologies and frameworks to be used in the system, including frontend, backend, and database technologies.
        hardware_requirements (str): A list of hardware specifications necessary to support the system, including CPU, GPU, RAM, and storage needs.
        interaction_interface (str): A description of the user interface and interaction mechanisms, such as web UI, voice interface, or control panels.
        test_optimization_plan (str): A strategy for testing and optimizing the system, including automated tests, performance monitoring, and user feedback integration.

    Returns:
        str: A comprehensive proposal outlining the system architecture, technology stack, hardware requirements, interaction interface, and test optimization plan.
    """
```'''
    mock_architectures = {'protask_single_tool_14': {'system_design': 'A three-tier website architecture with a presentation layer (React.js SPA), application layer (Node.js REST API), and a data layer (PostgreSQL database). Includes load balancing and CDN for global availability.', 'technology_stack': 'Frontend: React.js, Backend: Node.js with Express, Database: PostgreSQL, Hosting: AWS EC2 & S3, CDN: CloudFront', 'hardware_requirements': 'Cloud-based hosting infrastructure with 2 vCPUs, 8GB RAM for application servers, and RDS instance for database.', 'interaction_interface': 'Responsive web UI with intuitive navigation, accessible design (WCAG 2.1 compliance), and interactive dashboards.', 'test_optimization_plan': 'Automated testing with Jest and Cypress, performance monitoring with New Relic, and A/B testing for UX optimization.'}, 'protask_more_seq_tools_9': {'system_design': "A modular robotics simulation system integrating MATLAB's Computer Vision Toolbox for object detection and a Java-based simulation engine (e.g., jMonkeyEngine) for realistic physics interactions. The design supports plugin-based behavior modules for autonomous decision-making.", 'technology_stack': 'MATLAB for vision algorithms, Java with jMonkeyEngine for simulation, TCP/IP for inter-process communication, JSON for data exchange.', 'hardware_requirements': 'Development workstation with multi-core CPU, dedicated GPU (e.g., NVIDIA RTX 3060), 16GB RAM, and large SSD for storing simulation assets.', 'interaction_interface': 'Simulation control panel via Java Swing UI, real-time 3D visualization, and logging console for debugging.', 'test_optimization_plan': 'Benchmarking simulation frame rates, validating object detection accuracy against test datasets, and iterative tuning of physics parameters.'}, 'protask_more_seq_tools_13': {'system_design': 'A humanoid caregiver robot architecture with modular arms, mobility base, and AI-driven control system. Includes onboard sensors for navigation and human interaction, and cloud connectivity for updates.', 'technology_stack': 'Embedded C++ for motor control, ROS (Robot Operating System) for middleware, Python for AI modules, TensorFlow for object recognition, MQTT for cloud communication.', 'hardware_requirements': 'LIDAR sensor, stereo cameras, 6-DOF robotic arms, omnidirectional wheels, onboard CPU+GPU module (e.g., NVIDIA Jetson Xavier), battery pack with 6-hour runtime.', 'interaction_interface': 'Voice interface with speech-to-text and text-to-speech, touchscreen control panel, and gesture recognition module.', 'test_optimization_plan': 'Field testing in domestic environments, motion calibration, sensor fusion optimization, and user feedback-driven iteration.'}}
    if not system_design or not technology_stack:
        raise ValueError("Both 'system_design' and 'technology_stack' parameters are required.")
    matched_key = None
    for (key, data) in mock_architectures.items():
        if system_design.lower() in data['system_design'].lower() or technology_stack.lower() in data['technology_stack'].lower():
            matched_key = key
            break
    if matched_key:
        scenario = mock_architectures[matched_key]
        return f"System Architecture Proposal:\n- System Design: {scenario['system_design']}\n- Technology Stack: {scenario['technology_stack']}\n- Hardware Requirements: {scenario.get('hardware_requirements', 'N/A')}\n- Interaction Interface: {scenario.get('interaction_interface', 'N/A')}\n- Test & Optimization Plan: {scenario.get('test_optimization_plan', 'N/A')}\n"
    else:
        return f"System Architecture Proposal:\n- System Design: {system_design}\n- Technology Stack: {technology_stack}\n- Hardware Requirements: {hardware_requirements or 'N/A'}\n- Interaction Interface: {interaction_interface or 'N/A'}\n- Test & Optimization Plan: {test_optimization_plan or 'N/A'}\n"
if __name__ == '__main__':
    mcp.run(transport='stdio')