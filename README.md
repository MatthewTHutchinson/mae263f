# UCLA MAE 263F: Mechanics of Flexible Structures and Soft Robots

Coursework and project artifacts for UCLA MAE 263F, Fall 2025.

The repository collects Python simulations, written homework reports, and final
project materials for flexible structures, discrete elastic rods, and soft
robotics. Most assignments pair a compact numerical model with a final PDF
write-up that explains the mechanics, implementation, and results.

## Repository Map

| Folder | Topic | Main artifacts |
| --- | --- | --- |
| `homework_1/` | Spring-mass network simulation with explicit and implicit Euler integration | Python scripts, node/spring data, final report |
| `homework_2/` | Large-deformation beam simulation and Euler beam theory comparison | Beam simulation scripts, final report |
| `homework_3/` | Robotic control of an elastic beam with PI tracking | Control simulation script, final report |
| `homework_4/` | Close-coiled helical spring using a 3D discrete elastic rod model | DER simulation script, final report |
| `homework_5/` | Discrete elastic shell model of a cantilever plate under gravity | Shell simulation script, final report |
| `project/` | Course project proposal, midterm, final report, and presentation decks | PDFs and PowerPoint slides |

Each homework folder includes its own README with run notes and a description of
the assignment-specific files.

## Technical Themes

- Discrete mechanics for rods, beams, shells, springs, and flexible structures.
- Time integration, dynamic relaxation, damping, and Newton-style solves.
- Comparison between numerical models and classical analytical beam or spring
  formulas.
- Soft-robotics style control of deformable bodies through boundary conditions.
- Python-based scientific computing with NumPy and Matplotlib.

## Running The Code

Most homework scripts are standalone Python files. From a homework folder:

```bash
python HomeworkN.py
```

The common dependencies are:

```bash
pip install numpy matplotlib
```

Some scripts were written for a specific assignment environment and may assume
the included input files are present in the same folder.

## Notes

This is a public course-portfolio repository. It preserves the submitted reports
and implementation work, while the root README is intentionally a high-level map
to the more detailed per-assignment documentation.
