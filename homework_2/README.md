# Homework 2 – Large Deformation Beam Simulation

**Author**: Matthew Hutchinson  
**Course**: MAE 263 – Bionic Systems Engineering  
**Assignment**: Homework 2  
**Language**: Python (NumPy, Matplotlib)  
**Dependencies**: `numpy`, `matplotlib`

---

## 📘 Overview

This project simulates the deformation of a beam under various loading conditions using nonlinear finite element methods. The goal is to evaluate the accuracy and limitations of linear Euler beam theory by comparing it to the simulation results for both small and large deformations.

Key tasks include:
- Implementing time integration of a mass-spring beam using implicit Euler.
- Applying a point load at 0.75 m from the left end of the beam.
- Comparing simulation results to Euler beam theory for small deflections.
- Identifying divergence due to geometric nonlinearity at large deformations.

---

## 📂 File Structure

| File Name             | Description                                                                 |
|----------------------|-----------------------------------------------------------------------------|
| `homework2.py`       | Main simulation script for Question 1. Runs a single beam deflection test. |
| `homework2_q2.py`    | Modularized script for Question 2. Loops through multiple loads to compare with theory. |
| `objfun.py`          | Contains the Newton-Raphson solver and residual evaluation function.        |
| `HW2.pdf`            | Original problem statement (for reference).                                |
| `Homework2_HUTCHINSON.pdf` | Final report submission with plots, analysis, and answers.          |

---

## ▶️ How to Run

To run **Question 1** (single simulation with P = 2000 N):

```bash
python homework2.py
