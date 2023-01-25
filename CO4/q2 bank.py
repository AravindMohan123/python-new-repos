class Account:
    def __init__(self,AccNumber,name,type,balance):
        self.AccNumber = AccNumber
        self.name = name
        self.type = type
        self.balance = balance
    def withdraw(self,amount):
        self.balance -= amount
        return self.balance
    def deposit(self,amount):
        self.balance += amount
        return self.balance
    def transfer(self,amount,Account):
        self.balance -= amount
        Account.balance += amount

anum = int(input("account number"))
aname = input("account holder's name")
atype = input("account type")
abal = int(input("account balance"))
acc1 = Account(anum,aname,atype,abal)
print("propertise of "+ acc1.name , vars(acc1))

witdr = int(input("amount to be withdrawed"))
acc1.withdraw(witdr)
print("propertise of "+ acc1.name , vars(acc1))

depos = int(input("amount to be deposited"))
acc1.deposit(depos)
print("propertise of "+ acc1.name , vars(acc1))




