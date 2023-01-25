collist = []
n= int(input("enter the no of colors you want to enter"))
for i in range(n):
    
    collist.append(input("enter the color"))

print("the first and last colors entered are",collist[0],"and",collist[-1])    
