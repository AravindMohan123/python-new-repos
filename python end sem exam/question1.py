list1 = [1,2,3,4,[44,55,66,True],False,(34,56,78,89,34),{1,2,3,3,2,1},{1:34,"key2":[55,67,78,89],4:(45,22,61,34)},[56,'data science'],'Machine Learning']
#print(list1)
list2 = ['a',1,'b',2,'c',3,'d']
list3 = []
for i in list1:
    if(type(i) == int):
        list3.append(i)
    elif(type(i) == list):
        #print(i)
        for j in i:
            if(type(j) == int):
                list3.append(j)
    elif (type(i) == tuple):
         for k in i:
             list3.append(k)
    elif (type(i) == dict):
        for ky in i.keys():
            if(type(ky) == int):
                list3.append(ky)
            if(type(ky) == list):
                print(ky)
        for vl in i.values():
            if(type(vl) == int):
                list3.append(vl) 
            if(type(vl) == list):
                plist = list(vl)
                for cr in plist:
                    list3.append(cr)
                        
            if(type(vl) == tuple):
                for tr in vl:
                    list3.append(tr)

    elif type(i) == bool:
        if i == False:
            list3.append(0)
        else:
            list3.append(1)


print(list3)
product = 1    
for p in list3:
    product = product * p
   # print(product)
print('the product of' ,'\n',list3,'\n','is',product)

