
# Josephson Junction Simulator

## Motivation
As part of my Master's studies in Semiconductor Technology,I have a class in this simster which is  focus on superconductivity, I've been investigating Josephson junctions and their remarkable quantum properties. This project emerged from my desire to better understand the practical behavior of these superconducting devices through computational modeling.

Josephson junctions represent one of the most fascinating phenomena in superconductivity, where Cooper pairs tunnel through a barrier while maintaining quantum coherence. Through this simulation, I've explored both the DC Josephson effect (zero-voltage supercurrent) and AC Josephson effect (voltage-induced phase oscillations) that form the basis for many superconducting applications.
## output examples
![Josephson IV Curve](josephson_iv.png)

![Josephson dynamics curve](josephson_dynamics.png)

The first image shows how these quantum devices can carry electricity perfectly (with no voltage) up to a certain current, then suddenly switch to normal behavior. The second image reveals the hidden quantum oscillations that occur when we push them past this limit  these are what make Josephson junctions so useful for ultra-precise sensors and quantum computers.
## Features
This Python package simulates key aspects of Josephson junction physics:
- **DC Josephson Effect**: Models the supercurrent flow below critical current
- **AC Josephson Effect**: Simulates voltage oscillations when bias exceeds Ic
- **I-V Characteristics**: Visualizes the complete current-voltage relationship
- **Phase Dynamics**: Shows the time evolution of the quantum phase difference

## Physics Background
Josephson junctions exhibit:
1. **DC Josephson effect**: Supercurrent flows without voltage below critical current (I < Ic)
2. **AC Josephson effect**: Voltage oscillations occur when bias exceeds critical current (I > Ic)
3. **Macroscopic quantum phenomena**: The phase difference behaves as a quantum mechanical observable

## Installation
```bash
git clone https://github.com/Zeyad-Mustafa/josephson-junction.git
cd josephson-junction
python -m venv venv
source venv/bin/activate  # or venv\Scripts\activate on Windows
pip install -r requirements.txt
