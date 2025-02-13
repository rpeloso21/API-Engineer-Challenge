import matplotlib.pyplot as plt
from shapely.geometry import Polygon as ShapelyPolygon
from sympy import Point, Polygon as SymPyPolygon, pi, N
import numpy as np

points = [(0, 2), (2, 4), (4, 2), (2, 0)]  # Square



# The parse_input function would be used only if the data was given as a string in the exact manner shown in 
# the example.  You would then pass parse_input("(x1,y1) (x2,y2) (x3,y3) (x4,y4)") into the 
# calculate_quadrilateral function.
def parse_input(input_str):
    points = [
        tuple(map(int, pair.strip("()").split(","))) 
        for pair in input_str.split()
    ]
    return points


def calculate_area(points):

    polygon = ShapelyPolygon(points)
    area = polygon.area
    print(area)
    return area


def classify_quadrilateral_sympy(points):
    if len(points) != 4:
        return "Not a quadrilateral"

# -----  Find right angles -----
    poly = SymPyPolygon(*[Point(p) for p in points])

    angles = poly.angles.values()
    angles_degrees = [float(N(angle * 180 / pi)) for angle in angles]

    right_angles = all(np.isclose(angle, 90, atol=1e-6) for angle in angles_degrees)

# ----- Find parallel sides -----
    sides = poly.sides
    parallel_1_3 = sides[0].is_parallel(sides[2])
    parallel_2_4 = sides[1].is_parallel(sides[3])

# ----- Find equal sides -----
    lengths = [sides[i].length for i in range(4)]
    all_sides_equal = all(lengths[0] == length for length in lengths)
    opposite_sides_equal = lengths[0] == lengths[2] and lengths[1] == lengths[3]


    if right_angles:
        if all_sides_equal:
            return "Square"
        elif opposite_sides_equal:
            return "Rectangle"
        
    elif parallel_1_3 and parallel_2_4:
        if all_sides_equal:
            return "Rhombus"
        return "Parallelogram"
    
    elif parallel_1_3 or parallel_2_4:
        return "Trapezoid"
    
    elif ((np.isclose(lengths[0], lengths[1], atol=1e-6) and 
           np.isclose(lengths[2], lengths[3], atol=1e-6)) or 
          (np.isclose(lengths[1], lengths[2], atol=1e-6) and 
           np.isclose(lengths[3], lengths[0], atol=1e-6))):
        return "Kite"
    
    else:
        return "Other"
    

        

def graph_shape(p1, p2, p3, p4):
    x = [p1[0], p2[0], p3[0], p4[0]]
    y = [p1[1], p2[1], p3[1], p4[1]]

    x += (x[0],)
    y += (y[0],)

    plt.plot(x, y, marker='o', linestyle='-')
    plt.fill(x, y, alpha=0.3, color='blue')
    plt.xlabel("X-axis")
    plt.ylabel("Y-axis")
    plt.title("Polygon Shape")

    plt.grid()
    plt.show()



calculate_area(points)
print(classify_quadrilateral_sympy(points))
graph_shape((0, 2), (2, 4), (4, 2), (2, 0))