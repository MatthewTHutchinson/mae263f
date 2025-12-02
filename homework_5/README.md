# Homework 5 – Discrete Elastic Shells (Cantilever Plate under Gravity)

This repository contains my solution for **Homework 5** in MAE 263F / Discrete Elastic Shells.  
The goal is to model a thin rectangular plate as a discrete elastic shell, clamp it as a cantilever, load it with gravity, and compare the simulated tip deflection against the classical Euler–Bernoulli beam prediction.

---

## Contents

- `Homework5_HUTCHINSON.pdf`  
  My written report, including:
  - Derivation and description of the discrete shell model
  - Description of stretching and bending elements
  - Time integration and convergence criteria
  - Comparison between the simulated plate tip displacement and the Euler–Bernoulli analytical solution

- `Homework5.py`  
  Python implementation of the discrete elastic shell simulation, adapted from the course template code. It:
  - Builds a 2×10-node plate mesh matching the HW5 geometry
  - Constructs triangle connectivity with alternating diagonals
  - Builds stretching springs on all triangle edges
  - Builds bending hinges along all **interior edges** shared by two triangles (alternating diagonals + interior vertical edges)
  - Applies gravity and clamps the left edge
  - Time-steps the system using a semi-implicit scheme with Newton iterations
  - Tracks the tip displacement and compares it with Euler–Bernoulli theory

- `Homework5.pdf`  
  The original homework handout/instructions for reference.

---

## Problem Overview

We model a thin rectangular plate of length \(l\), width \(w\), and thickness \(h\) as a discrete shell:

- The plate is discretized into a **2×10 grid** of nodes (20 total).
- The left edge (all nodes at \(x = -0.0125\) m) is **clamped**.
- Gravity acts in the **negative \(z\)-direction**, loading the plate like a cantilevered beam.
- We are interested in the **steady-state vertical displacement** of the right-most bottom node (plate “tip”).

For comparison, the Euler–Bernoulli cantilever beam formula is used:

- Cross-sectional area: \( A = w h \)
- Second moment of area: \( I = \dfrac{w h^3}{12} \)
- Distributed load from gravity: \( q = \rho A g \)
- Tip deflection under uniform load:
  \[
  \delta_{EB} = -\dfrac{q l^4}{8 Y I}
  \]

---

## Implementation Details (Homework5.py)

### Discrete Shell Model

- **Stretching energy**  
  Each edge between two nodes \((i,j)\) has a stretching spring with stiffness:
  \[
  k_{s,k} = \frac{\sqrt{3}}{2} \, Y \, h \, \ell_k^2
  \]
  where \(\ell_k\) is the reference edge length.

- **Bending energy**  
  Each **hinge** is formed by an interior edge shared by two triangles, with nodes \((x_0, x_1, x_2, x_3)\) and hinge angle \(\theta(x_0,x_1,x_2,x_3)\).  
  The bending energy is:
  \[
  E_b = \frac{1}{2} k_b \left(\theta - \theta_{\text{bar}}\right)^2,
  \qquad
  k_b = \frac{2}{\sqrt{3}} \frac{Y h^3}{12}.
  \]
  The natural angle \(\theta_{\text{bar}}\) is taken from the flat configuration.

- **Mesh construction**
  - Nodes: 2 rows in \(y\), 10 nodes in \(x\), flattened into a 60-DOF vector.
  - Triangles: each quadrilateral cell is split into two triangles with **alternating diagonals** along the strip, matching the HW5 figure.
  - Stretching edges: all **unique triangle edges**.
  - Hinges: all **interior edges** (edges shared by exactly 2 triangles), which includes the alternating diagonals and the vertical interior edges.

### Dynamics and Time Integration

- Mass is lumped at the nodes with a uniform mass per node.
- External forces:
  - Gravity: \( \mathbf{F}_g = m \mathbf{g} \) at each node, with \(\mathbf{g} = (0, 0, -9.8)\) m/s².
- Damping:
  - Viscous damping term \( \mathbf{F}_v = -\nu \dfrac{\mathbf{q}^{n+1} - \mathbf{q}^n}{\Delta t} \) with \(\nu \approx 0.01\).
- Time stepping:
  - Semi-implicit scheme with Newton–Raphson iterations at each step.
  - Positions and velocities are updated as:
    \[
    \mathbf{u}^{n+1} = \frac{\mathbf{q}^{n+1} - \mathbf{q}^{n}}{\Delta t}.
    \]
- Boundary conditions:
  - All DOFs of the left-edge nodes are fixed (clamped).
  - Only the remaining “free” DOFs are updated each iteration.

---

## How to Run

### Requirements

- Python 3.x
- `numpy`
- `matplotlib`

Install dependencies (if needed):

```bash
pip install numpy matplotlib
