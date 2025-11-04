# Homework 3 — Robotic Control of an Elastic Beam  
**MAE 263F: Mechanics of Flexible Structures & Soft Robots**  
**Instructor:** Prof. Khalid Jawed  
**Student:** Matthew Hutchinson  
**Due Date:** November 5, 2025

---

## 📘 Overview

This project simulates the dynamic control of a slender elastic beam in 2D using a planar robotic end-effector. The goal is to drive the *middle node* of the beam along a desired trajectory by prescribing time-varying **Dirichlet boundary conditions** at the beam's tip—specifically:  
- Position: `x_c(t), y_c(t)`  
- Orientation: `θ_c(t)`  

The beam is modeled as a mass–spring chain with stretching and bending stiffness under the influence of gravity. Control is implemented through a **Proportional-Integral (PI)** controller.

---

## 📂 Folder Structure
homework_3/
│
├── Homework3_HUTCHINSON.pdf      # Final report (formatted per course requirements)
├── homework3.py                  # Main simulation file (run this)
├── README.md                     # This file

---

## ▶️ How to Run

1. Open `homework3.py` in your Python environment.
2. Run the script. It should require **no modification** to begin execution.
3. The simulation will:
   - Generate plots of beam deformation.
   - Log tracking errors and control inputs.
   - Display 5+ snapshots of the beam shape throughout the simulation.

Dependencies:
```bash
numpy
matplotlib
scipy
```
