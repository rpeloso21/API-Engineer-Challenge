import matplotlib.pyplot as plt
from shapely.geometry import Polygon as ShapelyPolygon
from sympy import Point, Polygon as SymPyPolygon, pi, N
import numpy as np
from main import classify_quadrilateral_sympy, calculate_area


test_cases = [
    # 1. 
    ([(1, 1), (1, 5), (5, 5), (5, 1)], "Square"),
    
    # 2. 
    ([(1, 1), (1, 5), (6, 5), (6, 1)], "Rectangle"),
    
    # 3. 
    ([(0, 2), (2, 4), (4, 2), (2, 0)], "Square"),
    
    # 4. 
    ([(0, 0), (3, 4), (7, 4), (4, 0)], "Parallelogram"),
    
    # 5. 
    ([(0, 0), (4, 3), (8, 3), (10, 0)], "Trapezoid"),
    
    # 6. 
    ([(0, 0), (2, 3), (4, 0), (2, -1)], "Kite"),
    
    # 7. 
    ([(0, 0), (2, 4), (5, 3), (3, -1)], "Parallelogram"),

    # 8.
    ([(0, 0), (3, 4), (6, 0), (3, -4)], "Rhombus"),

    #9
    ([(0, 0), (3, 4), (7, 3), (4, -2)], "Other"),

    #10
    ([(0, 0), (3, 4), (7, 3)], "Not a quadrilateral")
]

for points, expected in test_cases:
    result = classify_quadrilateral_sympy(points)
    area = calculate_area(points)
    print(f"Points: {points}\n  Area:{area}\n  Classified: {result} | Expected: {expected}\n")