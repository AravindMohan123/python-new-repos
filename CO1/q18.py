dicti1= {}
dicti2={}
s = int(input('enter the  size '))
for i in range(s):
    dicti1[i]=int(input('enter a number'))
for j in range(s,s*2):
    dicti2[j]=input('enter a word')



dicti1.update(dicti2)
print(dicti1)
