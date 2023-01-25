n=int(input("Enter a number"))
m=int(input("enter another number"))

if m>n:
    big =m
else:
    big =n
for i in range(1,big+1):
    if m%i==0 and n%i == 0:
        gcd=i

print("gcd is =",gcd)