class Square:
    square_list = []

    def __init__(self, per):
        self.p = per
        self.square_list.append(self.p)

    def s(self):
        return self.p * 4

s1 = Square(3)
s2 = Square(5)
s3 = Square(8)

print(Square.square_list)
