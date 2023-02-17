class Rectangle:

    def __init__(self,length,breadth):
        self.breadth = breadth
        self.length = length
        
    def  area(self):
        return self.length * self.breadth
    def per(self):
        return 2*(self.length + self.breadth)
l1=int(input('Enter the length of rectangle1'))
b1=int(input('Enter the breadths of rectangle1'))

l2=int(input('Enter the length of rectangle2'))
b2=int(input('Enter the breadth of rectangle2'))
rectangle1 = Rectangle(l1,b1)
rectangle2 = Rectangle(l2,b2)
pert = Rectangle(l1,b1)
pert1 = Rectangle(l2,b2)
print(pert.per())
print(pert1.per())
if rectangle1.area() > rectangle2.area():
    print("rectangle 1 is greater")
elif rectangle1.area() < rectangle2.area():
    print("rectangle 2 is greater"); 
else:
    print("both the rectangles are equal")
# if(rectangle1.area() > rectangle2.area()):
#     print("reactangle with length",rectangle1.lenght,"and breadth",rectangle1.breadth," is bigger")
# else:
#     print("reactangle with length",rectangle2.lenght,"and breadth",rectangle2.breadth," is bigger")
    

