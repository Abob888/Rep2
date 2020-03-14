class Square:
    square_list = []

    def __init__(self, per):
        self.p = per
        self.square_list.append(self.p * 4)

    def print_size(self):
        print('''{} to {} to {} to {}
              '''.format(self.p,
                         self.p,
                         self.p,
                         self.p))
        
s1 = Square(3)
s2 = Square(5)
s3 = Square(8)
s4 = Square(10)
s5 = Square(100)

s3.print_size()
