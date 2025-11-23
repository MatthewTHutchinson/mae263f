# Homework 1 - Spring Network Simulation

This repository contains a simulation of a spring-mass network using both **Implicit Euler** and **Explicit Euler** integration methods. The goal is to investigate stability, damping, and time integration behavior of dynamic spring systems under gravity.

---

## 📁 Contents

| File | Description |
|------|-------------|
| `Homework1_HUTCHINSON.pdf` | 📄 Final report with answers, analysis, plots, and comparison of methods. |
| `Homework1.py` | 🧠 **Implicit Euler** simulation of the spring network (main script). Uses Newton-Raphson and Hessians. |
| `explicit_euler.py` | ⚙️ **Explicit Euler** simulation. Standalone script to test stability with different `dt` values and damping. |
| `nodes.txt` | 📌 Node coordinates for the spring system (x, y). Each line is a node. |
| `springs.txt` | 🔗 Spring connections and stiffness. Format: node1, node2, stiffness. |

---

## ▶️ How to Run

Make sure you have Python 3 and `matplotlib` installed.

### 1. **Implicit Euler Simulation**
```bash
python Homework1.py
```
This will:
- Load `nodes.txt` and `springs.txt`
- Run the simulation with Implicit Euler
- Generate plots of node positions and figures of the network at specific times

### 2. **Explicit Euler Simulation**
```bash
python explicit_euler.py
```
This script:
- Initializes its own time step, damping, and simulation parameters
- Can be adjusted to test stability by changing `dt`
- Plots the motion of nodes over time and saves frames

---

## 📌 Notes
- Free degrees of freedom are predefined in each script.
- Simulation behavior is sensitive to `dt` due to stiffness and gravity.
- You can adjust:
  - Time step `dt`
  - Total simulation time
  - Damping coefficient `c` (in `explicit_euler.py`)
  - Plot frames and figure saving
