n = int(input("Enter the base of the triangle"))
for i in range(1,n):
    for j in range(1,i+1):
        print(j*i,end=" ")
    print("\r")