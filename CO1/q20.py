list1 = []
s = int(input('Enter the size of the list'))
for j in range(s):
    z=int(input('Enter the element'))
    list1.append(z) 
list2 =[]
for i in list1:
    if i % 2 != 0:
        list2.append(i)
print(list2)