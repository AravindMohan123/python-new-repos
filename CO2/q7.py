stri = input('Enter a word ending with"ing"')

if stri[-3:] == "ing":
    print(stri+"ly")
else:
    print(stri+"ing")
