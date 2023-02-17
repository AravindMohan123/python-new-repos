class student:
    def __init__(self,name,age,course,list1):
        self.name = name
        self.age = age
        self.course = course
        
        self.list1 = list(list1)
        
    def add(self):

        self.list1.append(self.name)
        self.list1.append(self.age)
        self.list1.append(self.course)
        return self.list1
    def display(self):
        print(self.list1)
        return self.list1
    



list1 = []
    
stud2 = student('mike',22,'cs',list1)  
c=5
i = 0    
while c != 0:
    print('choose from the following options')
    print('\n','0.Exit','\n','1.Add','\n','2.Display','\n','3.Search','\n','4.Delete','\n')
    c  = int(input('selected ='))
    if c == 1:
        a = input("Enter the name")
        b = input('Enter the age')
        c = input('Enter the course')
        stud1 = student(a,b,c,list1) 
        list1 = stud1.add()
    elif c==2:
        print(list1)
    elif c == 3:
        nm = input('Enter the name')
        for i in range(len(list1)):
            if list1[i] == nm:
                print('item found')
                print(nm,'\n')
                print(list1[i+1],'\n')
                print(list1[i+2], '\n')
                break
            else:
                print('item not found')
    elif c == 4:
        val= input('Enter the name to be deleted')
        for j in range(len(list1)):
            if list1[j] == val:
                print('item found') 
                list1[j] = 0
                list1[j+1] = 0
                list1[j+2] = 0
                print('item deleted successfully')
                break               
            else:
                print('item not found')
    else:
        print('Sorry wrong input')


