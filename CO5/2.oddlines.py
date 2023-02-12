a =open('abc.txt','r')
w =open('cpy.txt','w')
lines = (a.read().split('\n'))
for i in range(0,len(lines),2):
    w.write(lines[i]+"\n")
