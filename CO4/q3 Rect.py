class Rectangle:
    def __init__(self,length,breadth):
        self.__length = length
        self.__breadth = breadth
    def __lt__(self,other):
        area1 = self.__breadth * self.__length
        area2 = other.__breadth * other.__length
        return area1 < area2
    
a1 = Rectangle(5,6)
a2 = Rectangle(4,7)

print ()
print("a1>a2 :",a1>a2)
print("a2>a1:",a1<a2)

    