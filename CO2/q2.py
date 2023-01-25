n = int(input("Enter a limit"))
a=0
b=1
print(1)
for i in range(n):
    tmp = b    
    b =a+b
    a =tmp
    print(b)


    