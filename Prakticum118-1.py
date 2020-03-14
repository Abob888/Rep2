class Triangle():
    def __init__(self, a, h):
        self.basis = a
        self.high = h

    def area(self):
        return self.basis * self.high / 2

triangle = Triangle(11, 4)
print(triangle.area())
