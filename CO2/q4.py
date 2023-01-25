import math
start = 1000
end = 10000
l2=[]
for i in range(start,end):
    if math.sqrt(i)%1 == 0 and len([d for d in str(i) if int(d)%2!=0])==0:
        l2.append(i)
print(l2)