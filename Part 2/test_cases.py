import matplotlib.pyplot as plt
from shapely.geometry import Polygon as ShapelyPolygon
from sympy import Point, Polygon as SymPyPolygon, pi, N
import numpy as np
from main import classify_quadrilateral_sympy


test_cases = [
    # 1. Square: all right angles, all sides equal.
    ([(1, 1), (1, 5), (5, 5), (5, 1)], "Square"),
    
    # 2. Rectangle: all right angles, opposite sides equal (but not all sides equal).
    ([(1, 1), (1, 5), (6, 5), (6, 1)], "Rectangle"),
    
    # 3. Rhombus: no right angles, all sides equal and both pairs of opposite sides are parallel.
    ([(0, 2), (2, 4), (4, 2), (2, 0)], "Rhombus"),
    
    # 4. Parallelogram: no right angles, opposite sides equal and parallel.
    ([(0, 0), (3, 4), (7, 4), (4, 0)], "Parallelogram"),
    
    # 5. Trapezoid: one pair of parallel sides only.
    ([(0, 0), (4, 3), (8, 3), (10, 0)], "Trapezoid"),
    
    # 6. Kite: two distinct pairs of adjacent equal sides (but not all four equal).
    # Here, sides (0->1) and (1->2) are equal, and sides (2->3) and (3->0) are equal.
    ([(0, 0), (2, 3), (4, 0), (2, -1)], "Kite"),
    
    # 7. Other: an irregular quadrilateral that doesn't fit any special category.
    ([(0, 0), (2, 4), (5, 3), (3, -1)], "Other")
]

for points, expected in test_cases:
    result = classify_quadrilateral_sympy(points)
    print(f"Points: {points}\n  Classified: {result} | Expected: {expected}\n")