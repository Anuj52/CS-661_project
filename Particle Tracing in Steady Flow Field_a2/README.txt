CS661 – Assignment 3  
Particle Tracing in Steady Flow Field using RK4 Integration

---

## Team Details  
Group Number: 17
Roll Numbers: 210768, 210167

---

## Files Included
1. streamline_tracer.py – Python script to generate streamline using RK4 integration  
2. tornado3d_vector.vti – 3D vector field data (simulated tornado)  
3. output.vtp – Output streamline (generated from the seed point)  
4. README.txt – How to run and use the program

---

## Requirements
- Python 3.x 
- VTK library (pip install vtk)  
- ParaView (optional, for visualization)

---

## How to Run

1. Open a terminal (or the terminal in VS Code)  
2. Navigate to the folder containing the files  
3. Run the script using:

   ```bash
   python streamline_tracer.py x y z output.vtp