l1 = []
l2 = []
n= int(input("Enter the limit for list1"))
for i in range(n):
    a1 = int(input("Enter a number"))
    l1.append(a1)
n2= int(input("Enter the limit for list1"))
for i in range(n2):
    a2 = int(input("Enter a number"))
    l2.append(a2)
if len(l1) == len(l2):
    print ("the list are of same length")
else:
    print("The lists are not of the same length")
b=0    
for i in range(n):
    b=b+i;


d=0    
for i in range(n):
    d=d+i;
if b == d:
    print("The sum of elements in both the list are the same")
else:
    print("sorry different sum")
if set(l1).isdisjoint(set(l2)) == False:
   
    print(set(l1).intersection(set(l2)),"are the common elements")
else:
    
    print("No common elements found")
