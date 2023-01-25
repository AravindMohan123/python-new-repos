l1 = []
l2 = []
n = int(input("Enter the number of colors you want to enter" ))
for i in range(n):
    color1 = input("Enter a color")
    l1.append(color1);
n2= int(input("Enter the number of color you want to enter in list 2"))
for i in range(n2):
    color2 = input("Enter a color")
    l2.append(color2);

comm = set(l1).difference(set(l2))
print("the colors in list 1 and not in list2 are",comm)
