class Vector:
    def __init__(self: Vector, x: float, y: float):
        self.x = x
        self.y = y

    def __str__(self: Vector):
        return f'({self.x},{self.y})'

    def __add__(self: Vector, other: Vector):
        return Vector((self.x+other.x), (self.y+other.y))

v1 = Vector(2,3)
v2 = Vector(1, -2)
print(v1 + v2)