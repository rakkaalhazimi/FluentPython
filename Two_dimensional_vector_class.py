from math import hypot

'''Vector class implementing the operations just described, through the
    use of the special methods __repr__, __abs__, __add__ and __mul__.'''
class Vector:

    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def __repr__(self):
        return 'Vector(%r, %r)'%(self.x, self.y)

    def __abs__(self): # hypot mean pythagoras theorem
        return hypot(self.x, self.y)

    def __bool__(self):
        return bool(abs(self))

    def __add__(self, other):
        x = self.x + other.x
        y = self.y + other.y
        return Vector(x, y)

    def __mul__(self, scalar):
        return Vector(self.x * scalar, self.y * scalar)

'''Note how the + operator produces a Vector result, which is displayed in a friendly
    manner in the console.'''
v1 = Vector(2, 4)
v2 = Vector(2, 1)
print(v1 + v2)

'''The abs built-in function returns the absolute value of integers and floats, and the
magnitude of complex numbers, so to be consistent, our API also uses abs to calculate
the magnitude of a vector:'''
v = Vector(3, 4)
print(abs(v))
y = Vector(0, 0)
print(v.__bool__())
print(y.__bool__())
