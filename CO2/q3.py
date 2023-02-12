l1 = []
n = int(input("Enter the limit"))
for i in range(n):
    a = int(input("Enter the number"))
    l1.append(a)
c=0
for i in range(len(l1)):
    c = c+l1[i]

print("Sum is =",c)
