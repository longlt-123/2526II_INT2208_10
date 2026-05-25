import numpy as np

class Triangle:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c
    
    def is_valid_side(self):
        """Checks if the given side length is valid (positive number)."""
        for side in [self.a, self.b, self.c]:
            if not isinstance(side, (int)) or side <= 0 or side > 100:
                return False
        return True

    def is_triangle(self):
        """Returns True if the sides can form a triangle, False otherwise."""
        if not self.is_valid_side():
            return "Invalid side length"
        return (self.a + self.b > self.c) and (self.a + self.c > self.b) and (self.b + self.c > self.a)

    def type_of_triangle(self):
        """Returns the type of triangle formed by the sides."""
        if not self.is_valid_side():
            return "Invalid side length"
        
        if not self.is_triangle():
            return "Not a triangle"
        
        if self.a == self.b == self.c:
            return "Equilateral"
        elif self.a == self.b or self.b == self.c or self.a == self.c:
            return "Isosceles"
        else:
            return "Scalene"
