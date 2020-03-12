class Square():
    def __init__(self, s1):
        self.side = s1

    def change_size(self):
        return self.side + 5
        
squ = Square(3)
print(squ.change_size())
