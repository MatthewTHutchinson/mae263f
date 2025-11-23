# Homework 4 - Close-Coiled Helical Spring (DER)

This repository contains my solution for **Homework 4** for MAE 263F (Soft Robotics / Discrete Elastic Rods).  
The goal is to model a close-coiled helical spring using a 3D Discrete Elastic Rod (DER) formulation, use **dynamic relaxation** to find steady states, and compare the spring’s effective axial stiffness against the classical textbook formula.

---

## Contents

- `Homework4_HUTCHINSON.pdf`  
  Final write-up for Homework 4, including figures, discussion, and comparison to the textbook spring stiffness.

- `Homework4.py`  
  Main Python script that:
  - Builds the helical rod geometry from the given material and geometric parameters.  
  - Clamps the first two nodes and applies an axial force at the free end.  
  - Uses dynamic relaxation to integrate the DER equations of motion to a quasi-steady state.  
  - **Part (1):** Runs a single load case at \(F = F_{\text{char}}\) and plots tip displacement vs. time.  
  - **Part (2):** Sweeps the axial load over a range of values, extracts the steady tip displacement \(\delta_z^\ast(F)\), and fits a linear stiffness \(k\).  
  - **Part (3):** Repeats the stiffness extraction for several helix diameters \(D\), compares the numerical \(k(D)\) to the textbook prediction \(k_\text{text} = G d^4 / (8 N D^3)\), and generates the diameter-sweep plots.

- `Homework4.pdf`  
  Homework 4 prompt (provided by the instructor), included here for reference.

---

## Requirements

The script is written in Python and uses standard scientific libraries:

- Python 3.10
- `numpy`
- `matplotlib`
