z =[-1,-2,3,4,5,1,6]
l1 = [x for x in z if x > 0]
print(l1)


n = int(input("Enter a limit"))
l2 = [x*x for x in range(1,n) ]
print(l2)

v = input("Enter a word")
l3 = [x for x in v if x in "aeiou"]
print(l3)


l4 = [ord(x) for x in v ]
print(l4)



