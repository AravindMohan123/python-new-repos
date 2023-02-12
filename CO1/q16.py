string1 = input('Enter a string')
string2 = input('Enter a string')
string3= string2[0]+string1[1:len(string1)]+ " " + string1[0]+string2[1:len(string2)]
print(string3)
