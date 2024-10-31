"""This module contains a function to classify triangles based on their side lengths."""

def classify_triangle(side1: int, side2: int, side3: int) -> str:
    """Classifies a triangle based on its side lengths.

    Args:
        side1: The length of side 1.
        side2: The length of side 2.
        side3: The length of side 3.

    Returns:
        A string indicating the triangle type: 'Equilateral', 'Isosceles', 'Scalene', 
        'Right', 'NotATriangle', or 'InvalidInput'.

    Raises:
        ValueError: If any side length is not an integer or is non-positive.
    """

    if not all(isinstance(side, int) and side > 0 for side in (side1, side2, side3)):
        raise ValueError("Invalid input: Side lengths must be positive integers.")

    if side1 + side2 <= side3 or side1 + side3 <= side2 or side2 + side3 <= side1:
        return "NotATriangle"

    if side1 == side2 == side3:
        return "Equilateral"

    if side1**2 + side2**2 == side3**2:
        return "Right"

    if side1 == side2 or side1 == side3 or side2 == side3:
        return "Isosceles"

    return "Scalene"
