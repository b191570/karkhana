# Mobius Strip Modeling in Python

This project models a Möbius strip using parametric equations and computes key geometric properties: surface area and edge length. A 3D plot is also generated for visualization.

---

##  Objective

- Create a 3D mesh of a Möbius strip using parametric equations.
- Numerically approximate:
  - Surface Area
  - Edge Length
- Visualize the surface in 3D.

---

##  Parametric Equations Used

The Möbius strip is defined using the following parametric equations:

x(u, v) = (R + v * cos(u / 2)) * cos(u)
y(u, v) = (R + v * cos(u / 2)) * sin(u)
z(u, v) = v * sin(u / 2)


Where:
- `u ∈ [0, 2π]`
- `v ∈ [-w/2, w/2]`
- `R` = Radius from the center to the strip
- `w` = Width of the strip

---

##  Code Structure

The script contains a `MobiusStrip` class that:

- Accepts:
  - `R`: Radius
  - `w`: Width
  - `n`: Mesh resolution
- Computes:
  - A 3D grid of `(x, y, z)` points using NumPy
  - Surface Area using cross product of partial derivatives and `scipy.integrate.simpson`
  - Edge Length by summing distances along the boundary edges
- Displays a 3D plot using `matplotlib`
