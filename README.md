# engineering-simulations
Python-based simulation tool for structural analysis, including bending stress, shear force, bending moment, deflection, and vibration calculations with interactive visualizations.

# Engineering Simulations

## Overview
A Python-based simulation tool for structural analysis, designed to calculate and visualize:
- **Bending stresses**
- **Shear force and bending moment distributions**
- **Deflection curves**
- **Vibration analysis** (coming soon!)

The tool supports multiple load cases and beam configurations, providing insights into structural performance under various scenarios.

---

## Features
1. **Structural Analysis**:
   - Calculate bending stress, shear force, and bending moment for beams.
   - Visualize results with annotations for critical points.

2. **Dynamic Simulations** (Planned):
   - Simulate beam vibrations under dynamic loading.
   - Calculate natural frequencies and mode shapes.

3. **Interactive Visualizations**:
   - Use Matplotlib for static and Plotly/Dash for interactive plots.
---

## Getting Started
### Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/Srinivas26k/engineering-simulations.git
   cd engineering-simulations

2. Install dependencies:
    pip install -r requirements.txt

### Usage
    Run the beam_analysis.py script to calculate bending stresses, shear forces, and bending moments for a given beam.

### Contributions
    Contributions are welcome! Please fork the repo and submit a pull request.

---

## **Step 4: Add the `requirements.txt`**
    Add the following dependencies to `requirements.txt`:
    numpy 
    matplotlib 
    scipy 
    sympy   
    jupyter

    Install them locally:
    ```bash
    pip install -r requirements.txt

# Beam Analysis and Visualization

This repository contains Python scripts for analyzing and visualizing beam behavior under uniformly distributed loads. It calculates and plots **shear force**, **bending moment**, and **bending stress distributions** along the length of the beam. The project demonstrates structural mechanics concepts and visualization techniques, useful for engineering students and professionals.

## Features
- **Shear Force Distribution**: Calculates and plots the variation of shear force along the beam.
- **Bending Moment Distribution**: Computes and visualizes the bending moment curve.
- **Stress Analysis**: Evaluates bending stresses based on moment of inertia and neutral axis distance.
- **Annotations on Graphs**: Highlights key points like maximum shear force, zero shear force, and maximum bending moment.


## Installation
### Prerequisites
- Python 3.7+
- `matplotlib` library for plotting

### Steps
1. Clone the repository:
   ```bash
   git clone https://github.com/Srinivas26k/engineering-simulations.git
   cd beam-analysis

2. Install required Python libraries:
    bash
    Copy code
    pip install matplotlib

### Usage 
1. Test the Calculations
   Run the test_script.py to verify the shear force, bending moment, and stress calculations:
   ```bash
   Copy code
   python tests/test_script.py
---
2. Visualize the Results
   Generate and view plots for shear force and bending moment distributions:
   ```bash
   Copy code
   python visualization/visualize_results.py
   The plots will be saved in the results/ directory.
----
3. Customize Beam Parameters
   You can modify the beam length, load intensity, and cross-section dimensions in test_script.py or visualize_results.py to analyze different cases.
   Example Output
   Shear Force Distribution
    Bending Moment Distribution

 ## Applications
   Engineering coursework or research in structural analysis.
   Practical applications for designing beams in civil and mechanical engineering.
   Contributing
   Pull requests are welcome! If you want to contribute to this project:

## Fork the repository.
   Create a feature branch (git checkout -b feature-name).
   Commit your changes (git commit -m 'Add some feature').
   Push to your branch (git push origin feature-name).
   Open a pull request.
   
   License
   This project is licensed under the MIT License. See LICENSE for details.

### Contact
    For any questions or suggestions, reach out to:

    Name: Srinivas
    LinkedIn: Your LinkedIn Profile





