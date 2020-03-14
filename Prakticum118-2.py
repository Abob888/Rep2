class Hexagon:
    def __init__(self, lenght):
        self.hex_lenght = lenght

    def calculate_perimeter(self):
        return self.hex_lenght * 6

gran = Hexagon(5)
print(gran.calculate_perimeter())
