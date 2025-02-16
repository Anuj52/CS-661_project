import vtk

def render_volume_with_shading(filename, use_shading=False, window_size=(1000, 1000)):
    # Create a reader for XML image data
    reader = vtk.vtkXMLImageDataReader()
    reader.SetFileName(filename)
    reader.Update()

    # Create and set up the color transfer function
    colorTF = vtk.vtkColorTransferFunction()
    colorTF.AddRGBPoint(-4931.54, 0.0, 1.0, 1.0)
    colorTF.AddRGBPoint(-2508.95, 0.0, 0.0, 1.0)
    colorTF.AddRGBPoint(-1873.90, 1.0, 0.0, 0.5)
    colorTF.AddRGBPoint(-1027.16, 1.0, 0.0, 0.0)
    colorTF.AddRGBPoint(-298.031, 1.0, 0.4, 0.0)
    colorTF.AddRGBPoint(2594.97, 1.0, 1.0, 0.0)

    # Create and set up the opacity transfer function
    opacityTF = vtk.vtkPiecewiseFunction()
    opacityTF.AddPoint(-4931.54, 1.0)
    opacityTF.AddPoint(101.815, 0.002)
    opacityTF.AddPoint(2594.97, 0.0)

    # Set up volume properties
    volumeProperty = vtk.vtkVolumeProperty()
    volumeProperty.SetColor(colorTF)
    volumeProperty.SetScalarOpacity(opacityTF)
    volumeProperty.SetInterpolationTypeToLinear()

    # Enable or disable shading based on the input parameter
    if use_shading:
        volumeProperty.ShadeOn()
        volumeProperty.SetAmbient(0.5)
        volumeProperty.SetDiffuse(0.5)
        volumeProperty.SetSpecular(0.5)
        volumeProperty.SetSpecularPower(10)
    else:
        volumeProperty.ShadeOff()

    # Set up the volume mapper
    volumeMapper = vtk.vtkSmartVolumeMapper()
    volumeMapper.SetInputConnection(reader.GetOutputPort())
    volumeMapper.SetSampleDistance(1.0)

    # Create the volume and set its mapper and property
    volume = vtk.vtkVolume()
    volume.SetMapper(volumeMapper)
    volume.SetProperty(volumeProperty)

    # Create an outline of the volume
    outlineFilter = vtk.vtkOutlineFilter()
    outlineFilter.SetInputConnection(reader.GetOutputPort())
    
    outlineMapper = vtk.vtkPolyDataMapper()
    outlineMapper.SetInputConnection(outlineFilter.GetOutputPort())
    
    outlineActor = vtk.vtkActor()
    outlineActor.SetMapper(outlineMapper)
    outlineActor.GetProperty().SetColor(1, 1, 1)

    # Set up the renderer
    renderer = vtk.vtkRenderer()
    renderer.AddVolume(volume)
    renderer.AddActor(outlineActor)
    renderer.SetBackground(0.1, 0.1, 0.2)

    # Set up the render window
    renderWindow = vtk.vtkRenderWindow()
    renderWindow.AddRenderer(renderer)
    renderWindow.SetSize(*window_size)

    # Set up the interactor
    interactor = vtk.vtkRenderWindowInteractor()
    interactor.SetRenderWindow(renderWindow)

    # Reset the camera to fit the data
    renderer.ResetCamera()
    
    print("Rendering... Close the window to exit.")
    
    # Render the scene
    renderWindow.Render()
    
    # Start the interaction
    interactor.Start()

if __name__ == "__main__":
    import argparse
    
    # Set up command-line argument parsing
    parser = argparse.ArgumentParser(description="Volume Rendering with optional Phong Shading.")
    
    parser.add_argument("filename", type=str, help="Path to the .vti file to be rendered.")
    
    parser.add_argument("--use_shading", action="store_true", help="Enable Phong shading (default: off).")
    
    args = parser.parse_args()

    # Call the main function with parsed arguments
    render_volume_with_shading(filename=args.filename, use_shading=args.use_shading)
