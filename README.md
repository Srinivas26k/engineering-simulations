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

## Project Structure
engineering-simulations/
│
├── src/                   # Source code
│   ├── beam_analysis.py    # Core calculations
│   ├── plot_visuals.py     # Visualization functions
│   └── utils.py            # Utility functions
│
├── tests/                 # Unit tests
├── notebooks/             # Jupyter notebooks for demonstrations
├── docs/                  # Documentation files
│   ├── installation.md
│   └── usage.md
│
├── README.md              # Project description
├── requirements.txt       # Python dependencies
└── LICENSE                # License file


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
