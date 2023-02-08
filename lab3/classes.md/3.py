class Shape():
    def __init__(self):
        pass
    def area(self, length, width):
        return 0
class Rectangle(Shape):
    def __init__(self,length,width):
        self.l = length
        self.w = width
    def area(self):
        return self.l*self.w
a = int(input())
b = int(input())
s = Rectangle(a,b).area()
print(s)
# or we can print it like this:
l = [s]
for i in l:
    print(i)