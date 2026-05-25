import pytest
from triangle import Triangle

def test_valid_side():
    assert Triangle(5, 5, 5).is_valid_side() == True
    assert Triangle(1, 1, 1).is_valid_side() == True
    assert Triangle(100, 100, 100).is_valid_side() == True

    assert Triangle(-1, -1, -1).is_valid_side() == False
    assert Triangle(0, 0, 0).is_valid_side() == False
    assert Triangle(101, 101, 101).is_valid_side() == False

    assert Triangle(1, 5, 1.4).is_valid_side() == False
    assert Triangle(5, 5, -5.5).is_valid_side() == False
    assert Triangle(5, -3, 100.5).is_valid_side() == False
    assert Triangle(7.5, 6.5, 5.5).is_valid_side() == False

def test_is_triangle():
    assert Triangle(5, 5, 5).is_triangle() == True
    assert Triangle(3, 4, 5).is_triangle() == True

    assert Triangle(1, 1, 2).is_triangle() == False
    assert Triangle(1, 2, 3).is_triangle() == False
    assert Triangle(10, 1, 1).is_triangle() == False
    assert Triangle(5, 5, 10).is_triangle() == False

    assert Triangle(0, 0, 0).is_triangle() == "Invalid side length"
    assert Triangle(-1, -1, -1).is_triangle() == "Invalid side length"
    assert Triangle(101, 101, 101).is_triangle() == "Invalid side length"
    assert Triangle(1, 5, 1.4).is_triangle() == "Invalid side length"
    assert Triangle(5, 5, -5.5).is_triangle() == "Invalid side length"

def test_type_of_triangle():
    assert Triangle(5, 5, 5).type_of_triangle() == "Equilateral"
    assert Triangle(5.5, 5.5, 5.5).type_of_triangle() == "Invalid side length"

    assert Triangle(3, 4, 5).type_of_triangle() == "Scalene"
    assert Triangle(3.6, 4, 5).type_of_triangle() == "Invalid side length"

    assert Triangle(5, 5, 3).type_of_triangle() == "Isosceles"
    assert Triangle(5.3, 5.3, 3).type_of_triangle() == "Invalid side length"

    assert Triangle(1, 1, 2).type_of_triangle() == "Not a triangle"
    assert Triangle(1, 2, 3).type_of_triangle() == "Not a triangle"
    assert Triangle(10, 1, 1).type_of_triangle() == "Not a triangle"
    assert Triangle(5, 5, 10).type_of_triangle() == "Not a triangle"

    assert Triangle(0, 0, 0).type_of_triangle() == "Invalid side length"
    assert Triangle(-1, -1, -1).type_of_triangle() == "Invalid side length"
    assert Triangle(101, 101, 101).type_of_triangle() == "Invalid side length"
    assert Triangle(1, 5, 1.4).type_of_triangle() == "Invalid side length"
    assert Triangle(5, 5, -5.5).type_of_triangle() == "Invalid side length"