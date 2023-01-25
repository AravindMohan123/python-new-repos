string1 = input("Enter a string")

print(string1[0]+string1[1:len(string1)].replace(string1[0],"$"))
