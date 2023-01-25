stri = "hello world"
count =0
l1 =list(stri)
for i in set(l1)-set(" S"):
    print(i, ':',l1.count(i))
    