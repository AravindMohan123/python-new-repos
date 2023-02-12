l = []
print("number of times a repeated")
for j in range(6):
	name = input("enter the name")
	l.append(name)
for i in l:
	print(i , ":",i.count("a"))
