class Rectangle:

    def __init__(self,length,breadth):
        self.breadth = breadth
        self.length = length
        
    def  area(self):
        return self.length * self.breadth

rectangle1 = Rectangle(2,6)
rectangle2 = Rectangle(4,7)
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
    

