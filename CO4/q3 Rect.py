class Rectangle:
    def __init__(self,length,breadth):
        self.__length = length
        self.__breadth = breadth
    def __lt__(self,other):
        area1 = self.__breadth * self.__length
        area2 = other.__breadth * other.__length
        return area1 < area2


x1=int(input('Enter l1'))
y1=int(input('Enter b1'))
x2=int(input('Enter l2'))
y2=int(input('Enter b2'))


    
a1 = Rectangle(x1,y1)
a2 = Rectangle(x2,y2)

print ()
print("a1>a2 :",a1>a2)
print("a2>a1:",a1<a2)

    
