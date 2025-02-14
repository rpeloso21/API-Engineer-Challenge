import matplotlib.pyplot as plt
from shapely.geometry import Polygon as ShapelyPolygon
from sympy import Point, Polygon as SymPyPolygon, pi, N
import numpy as np

# Input XY points here:
points = [(0, 0), (3, 4), (7, 3), (4, -2)]


def calculate_area(points):

    try:
        polygon = ShapelyPolygon(points)
        area = polygon.area

        if classify_quadrilateral_sympy(points) == "Other":
            return -1
        
        elif classify_quadrilateral_sympy(points) == "Not a quadrilateral":
            return -1
        
        else:
            return area
        
    except Exception as e:
        print(f"Unexpected calculation error: {e}")


def classify_quadrilateral_sympy(points):
    if len(points) != 4:
        return "Not a quadrilateral"
    
    try:
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
        lengths = [float(N(sides[i].length)) for i in range(4)]
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
        
        elif ((np.isclose(lengths[0], lengths[1], atol=1e-6) and np.isclose(lengths[2], lengths[3], atol=1e-6)) or 
            (np.isclose(lengths[1], lengths[2], atol=1e-6) and np.isclose(lengths[3], lengths[0], atol=1e-6))):
            return "Kite"
        
        else:
            return "Other"
        
    except Exception as e:
        print(f"Unexpected classification error: {e}")
    
    
def graph_shape(points):
    try:
        p1, p2, p3, p4 = [point for point in points]

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

    except Exception as e:
        print(f"Unexpected graphing error: {e}")


if __name__ == "__main__":
    try: 
        print(f"{classify_quadrilateral_sympy(points)} {calculate_area(points)}")
        graph_shape(points)

    except Exception as e:
        print(f"Unexpected exception {e}")

