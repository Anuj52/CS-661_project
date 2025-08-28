import vtk
import sys
import numpy as np

def is_in_bounds(point, bounds):
    x, y, z = point
    x_min, x_max, y_min, y_max, z_min, z_max = bounds
    return x_min <= x <= x_max and y_min <= y <= y_max and z_min <= z <= z_max

def rk4_step(point, step_size, interpolator):
    def get_vector(p):
        interpolator.SetSourceData(vector_data)
        interpolator.SetInputData(vtk.vtkPolyData())
        interpolator.Update()
        probe = vtk.vtkProbeFilter()
        pt = vtk.vtkPoints()
        pt.InsertNextPoint(p)
        poly = vtk.vtkPolyData()
        poly.SetPoints(pt)
        probe.SetSourceData(vector_data)
        probe.SetInputData(poly)
        probe.Update()

        result = probe.GetOutput()
        vectors = result.GetPointData().GetVectors()
        if vectors and vectors.GetNumberOfTuples() > 0:
            return np.array(vectors.GetTuple(0))
        else:
            return None

    k1 = get_vector(point)
    if k1 is None: return None
    k2 = get_vector(point + 0.5 * step_size * k1)
    if k2 is None: return None
    k3 = get_vector(point + 0.5 * step_size * k2)
    if k3 is None: return None
    k4 = get_vector(point + step_size * k3)
    if k4 is None: return None

    return point + (step_size / 6.0) * (k1 + 2*k2 + 2*k3 + k4)

def trace_streamline(seed, direction, step_size, max_steps, bounds, interpolator):
    points = []
    current = np.array(seed)

    for _ in range(max_steps):
        if not is_in_bounds(current, bounds):
            break
        points.append(tuple(current))
        next_point = rk4_step(current, direction * step_size, interpolator)
        if next_point is None:
            break
        current = next_point

    return points

def build_polyline(points):
    poly_data = vtk.vtkPolyData()
    vtk_points = vtk.vtkPoints()
    lines = vtk.vtkCellArray()

    for i, pt in enumerate(points):
        vtk_points.InsertNextPoint(pt)
    lines.InsertNextCell(len(points))
    for i in range(len(points)):
        lines.InsertCellPoint(i)

    poly_data.SetPoints(vtk_points)
    poly_data.SetLines(lines)
    return poly_data

if __name__ == "__main__":
    if len(sys.argv) != 5:
        print("Usage: python streamline_tracer.py x y z output.vtp")
        sys.exit(1)

    # Inputs
    seed = tuple(map(float, sys.argv[1:4]))
    output_file = sys.argv[4]
    step_size = 0.05
    max_steps = 1000

    # Read vector field
    reader = vtk.vtkXMLImageDataReader()
    reader.SetFileName("tornado3d_vector.vti")
    reader.Update()
    vector_data = reader.GetOutput()

    bounds = vector_data.GetBounds()

    # Interpolator
    interpolator = vtk.vtkProbeFilter()

    # Backward
    backward = trace_streamline(seed, -1, step_size, max_steps, bounds, interpolator)
    backward.reverse()

    # Forward
    forward = trace_streamline(seed, 1, step_size, max_steps, bounds, interpolator)

    full_path = backward + [seed] + forward
    streamline_polydata = build_polyline(full_path)

    # Write to .vtp
    writer = vtk.vtkXMLPolyDataWriter()
    writer.SetFileName(output_file)
    writer.SetInputData(streamline_polydata)
    writer.Write()

    print(f"Streamline written to {output_file}")
