import vtk

# Function to interpolate between two points based on scalar values
def interpolate(p1, p2, s1, s2, iso):
    if s2 == s1:
        return p1
    t = (iso - s1) / (s2 - s1)
    x = p1[0] + t * (p2[0] - p1[0])
    y = p1[1] + t * (p2[1] - p1[1])
    z = p1[2] + t * (p2[2] - p1[2])
    return (x, y, z)

# Read the VTK image data file
reader = vtk.vtkXMLImageDataReader()
reader.SetFileName("Isabel_2D.vti")
reader.Update()
image_data = reader.GetOutput()

# Get image properties
dims = image_data.GetDimensions()
origin = image_data.GetOrigin()
spacing = image_data.GetSpacing()

# Get scalar values
scalars = image_data.GetPointData().GetScalars()

# Set isovalue and output filename
iso_value = -250
output_filename = f"output_{iso_value}.vtp"

# Initialize VTK objects for storing contour data
contour_points = vtk.vtkPoints()
lines = vtk.vtkCellArray()

# Get dimensions of the 2D image
nx, ny, _ = dims

# Iterate through each cell in the image
for j in range(ny - 1):
    for i in range(nx - 1):
        # Calculate indices for the four corners of the cell
        idx0 = i + j * nx
        idx1 = (i + 1) + j * nx
        idx2 = (i + 1) + (j + 1) * nx
        idx3 = i + (j + 1) * nx

        # Get scalar values for the four corners
        s0 = scalars.GetTuple1(idx0)
        s1 = scalars.GetTuple1(idx1)
        s2 = scalars.GetTuple1(idx2)
        s3 = scalars.GetTuple1(idx3)

        # Calculate coordinates for the four corners
        p0 = (origin[0] + i * spacing[0], origin[1] + j * spacing[1], origin[2])
        p1 = (origin[0] + (i + 1) * spacing[0], origin[1] + j * spacing[1], origin[2])
        p2 = (origin[0] + (i + 1) * spacing[0], origin[1] + (j + 1) * spacing[1], origin[2])
        p3 = (origin[0] + i * spacing[0], origin[1] + (j + 1) * spacing[1], origin[2])

        # Store intersections
        intersections = []
        edges = [
            (p0, p1, s0, s1),
            (p1, p2, s1, s2),
            (p2, p3, s2, s3),
            (p3, p0, s3, s0)
        ]

        # Check for intersections on each edge of the cell
        for (p_start, p_end, scalar_start, scalar_end) in edges:
            if (scalar_start - iso_value) * (scalar_end - iso_value) < 0:
                intersection_point = interpolate(p_start, p_end, scalar_start, scalar_end, iso_value)
                intersections.append(intersection_point)

        # Create line segments for the contour
        if len(intersections) == 2:
            pt_id0 = contour_points.InsertNextPoint(intersections[0])
            pt_id1 = contour_points.InsertNextPoint(intersections[1])
            line = vtk.vtkLine()
            line.GetPointIds().SetId(0, pt_id0)
            line.GetPointIds().SetId(1, pt_id1)
            lines.InsertNextCell(line)
        elif len(intersections) == 4:
            for k in range(0, 4, 2):
                pt_id0 = contour_points.InsertNextPoint(intersections[k])
                pt_id1 = contour_points.InsertNextPoint(intersections[k+1])
                line = vtk.vtkLine()
                line.GetPointIds().SetId(0, pt_id0)
                line.GetPointIds().SetId(1, pt_id1)
                lines.InsertNextCell(line)

# Create a polydata object to store the contour
contour_polydata = vtk.vtkPolyData()
contour_polydata.SetPoints(contour_points)
contour_polydata.SetLines(lines)

# Write the contour to a VTP file
writer = vtk.vtkXMLPolyDataWriter()
writer.SetFileName(output_filename)
writer.SetInputData(contour_polydata)
writer.Write()

print(f"Isocontour extraction complete. Output saved as '{output_filename}'.")
