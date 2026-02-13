# Interactive 3D Rubik’s Cube Simulator

A small Python project that renders and animates a fully interactive 3D Rubik’s Cube using **PyVista** and **PyVistaQt**.  
The cube can be rotated in real time using keyboard controls, making it a simple demonstration of 3D transformations, mesh manipulation, and event-driven animation in Python.

---

## ✨ Features

- 3D Rubik’s Cube visualization
- Smooth animated face rotations
- Keyboard-controlled interaction
- Uses GPU-accelerated rendering via VTK (through PyVista)
- Modular rotation system using transformation matrices

---

## 🛠️ Tech Stack

- Python 3
- PyVista
- PyVistaQt
- NumPy
- VTK (via PyVista)

---

## Installation

### 1. Clone the repository

```bash
git clone https://github.com/your-username/your-repo-name.git
cd your-repo-name
```

### 2. Install dependencies

```bash
pip install pyvista pyvistaqt numpy
```

## Usage

Run the main script:

```bash
python cube_main.py
```

A window will open showing the 3D cube.

## Controls

Each key rotates one face of the cube.

| Key | Action |
| :--- | :--- |
| **L / Shift+L** | Right face rotation |
| **J / Shift+J** | Left face rotation |
| **I / Shift+I** | Top face rotation |
| **K / Shift+K** | Bottom face rotation |
| **O / Shift+O** | Front face rotation |
| **U / Shift+U** | Back face rotation |

Uppercase keys rotate in the opposite direction.

## Project Structure

```code
cube_main.py   # Main application and cube logic
```

## Purpose

This project was created as a small experiment to explore:
	•	3D rendering in Python
	•	Transformation matrices
	•	Event-driven graphics programming
	•	Visualization libraries beyond traditional GUI frameworks

## Possible Improvements

  • Full scramble / solve logic
	•	Mouse-based rotation
	•	Cube size configuration (NxN cubes)
	•	GUI overlay
	•	Save / load cube state











