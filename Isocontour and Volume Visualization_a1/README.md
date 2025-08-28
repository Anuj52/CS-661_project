# for 2D_Isocontour_Extraction.py
## 2D Isocontour Extraction using VTK

This script extracts isocontours from a 2D VTK image data file (.vti) using the marching squares algorithm and saves the result as a VTK PolyData file (.vtp).

### Features

- Reads 2D VTK image data (.vti files)
- Extracts isocontours for a specified isovalue
- Implements the marching squares algorithm
- Saves the resulting contours as a VTK PolyData file (.vtp)


### Requirements

- Python 3.x
- VTK (Visualization Toolkit) library


### Installation

1. Ensure you have Python 3.x installed on your system.
2. Install VTK using pip:
```
pip install vtk
```


### Usage

1. Place your input .vti file in the same directory as the script.
2. Modify the script to set the desired isovalue and input filename:
```python
iso_value = -250  # Set your desired isovalue here
reader.SetFileName("Isabel_2D.vti")  # Set your input filename here
```

3. Run the script:
```
python script_name.py
```


### Output

The script will generate a .vtp file named `output_{iso_value}.vtp` in the same directory, where `{iso_value}` is the specified isovalue.

### Customization

You can modify the following parameters in the script:

- `iso_value`: The isovalue for contour extraction
- Input filename: Change the filename in `reader.SetFileName()`


### Note

This script assumes a 2D image data input. For 3D volumes, the algorithm would need to be extended to implement marching cubes instead of marching squares.

# For volume_render.py 
## Volume Rendering with VTK

This Python script uses the Visualization Toolkit (VTK) to render volumetric data from a .vti file. It provides options for rendering with or without Phong shading.

### Features

- Renders volumetric data from .vti files
- Customizable color and opacity transfer functions
- Optional Phong shading for enhanced depth perception
- Adjustable window size
- Outline display of the volume boundaries


### Requirements

- Python 3.x
- VTK (Visualization Toolkit) library


### Installation

1. Ensure you have Python 3.x installed on your system.
2. Install VTK using pip:
```
pip install vtk
```


### Usage

Run the script from the command line with the following syntax:

```
python script_name.py filename [--use_shading]
```

- `filename`: Path to the .vti file you want to render
- `--use_shading`: (Optional) Enable Phong shading for enhanced depth perception


### Example

```
python volume_render.py Isabel_3D.vti --use_shading
```

This command will render the volume data from 'Isabel_3D.vti' with Phong shading enabled.

### Customization

You can modify the following parameters in the script:

- Color transfer function (`colorTF`)
- Opacity transfer function (`opacityTF`)
- Shading properties (ambient, diffuse, specular)
- Window size


### Controls

- Rotate: Click and drag with the left mouse button
- Pan: Click and drag with the middle mouse button
- Zoom: Use the mouse wheel or click and drag with the right mouse button


### Note

Close the rendering window to exit the program.

### License

This script is provided as-is under the MIT License. Feel free to modify and distribute it as needed.