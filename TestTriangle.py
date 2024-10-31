"""This module contains unit tests for the classify_triangle function."""

import unittest
from Triangle import classify_triangle  # Ensure the function name matches the one in Triangle.py

class TestTriangles(unittest.TestCase):
    """Unit tests for the classify_triangle function."""

    def test_right_triangle_a(self):
        """Test for a right triangle with sides 3, 4, 5."""
        self.assertEqual(
            classify_triangle(3, 4, 5), 'Right', '3,4,5 is a Right triangle'
        )

    def test_right_triangle_b(self):
        """Test for a right triangle with sides 5, 3, 4."""
        self.assertEqual(
            classify_triangle(5, 3, 4), 'Right', '5,3,4 is a Right triangle'
        )

    def test_equilateral_triangles(self):
        """Test for an equilateral triangle with all sides equal."""
        self.assertEqual(
            classify_triangle(1, 1, 1), 'Equilateral', '1,1,1 should be equilateral'
        )

    def test_isosceles_triangle(self):
        """Test for an isosceles triangle with two equal sides."""
        self.assertEqual(
            classify_triangle(2, 2, 3), 'Isosceles', '2,2,3 should be isosceles'
        )

    def test_scalene_triangle(self):
        """Test for a scalene triangle with all sides different."""
        self.assertEqual(
            classify_triangle(3, 4, 6), 'Scalene', '3,4,6 should be scalene'
        )

    def test_invalid_input(self):
        """Test for invalid inputs."""
        self.assertEqual(
            classify_triangle(201, 3, 4), 'InvalidInput', '201,3,4 should be invalid input'
        )
        self.assertEqual(
            classify_triangle(-1, 2, 3), 'InvalidInput', '-1,2,3 should be invalid input'
        )
        self.assertEqual(
            classify_triangle(1.5, 2, 3), 'InvalidInput', '1.5,2,3 should be invalid input'
        )

    def test_not_a_triangle(self):
        """Test for inputs that do not form a triangle."""
        self.assertEqual(
            classify_triangle(1, 1, 3), 'NotATriangle', '1,1,3 is not a triangle'
        )

if __name__ == '__main__':
    print('Running unit tests')
    unittest.main()

# Ensure there's a final newline at the end of the file