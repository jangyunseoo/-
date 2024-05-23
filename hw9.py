class Rectangle:
    def __init__(self, x1, y1, x2, y2):
        if x1 < x2 and y1 < y2 :
            self.__lt = x1, y1
            self.__rb = x2, y2
        
    def show(self):
        print(f'좌측 상단 꼭지점이 {self.__lt}이고 우측 하단 꼭지점이 {self.__rb}인 사각형입니다.')

    def getWidth(self):
        x1, _ = self.__lt
        x2, _ = self.__rb
        return x2 - x1

    def getHeight(self):
        _, y1 = self.__lt
        _, y2 = self.__rb
        return y2 - y1

    def getArea(self):
        return self.getWidth() * self.getHeight()

    def getPerimeter(self):
        return (self.getWidth() * 2) + (self.getHeight() * 2)

r1 = Rectangle(5, 5, 20, 10)
a = r1.getArea()
p = r1.getPerimeter()

r1.show()
print(f'\n넓이는 {a}, 둘레는 {p}')
