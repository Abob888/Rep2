class Lion():
    def __init__(self, n):
        self.name = n

    def __repr__(self):
        return self.name

lion = Lion('Gilbert')
print(lion)

class AlwaysPositive:
    def __init__(self, number):
        self.n = number

    def __add__(self, other):
        return abs(self.n + other.n)
    
x = AlwaysPositive(-20)
y = AlwaysPositive(10)

print(x + y)
