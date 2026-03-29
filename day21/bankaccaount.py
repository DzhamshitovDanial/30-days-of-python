class   Bankaccaount:
    def __init__(self,holder,balance):
        self.holder=holder
        self.balance=balance
    def add_balance(self,n):
        self.balance=self.balance+n
    def withdraw(self,n):
        if self.balance-n>=0:
            self.balance=self.balance-n
        else:
            print('error')
    def show_balance(self):
        return self.balance
user1=Bankaccaount('Danial',1000000000)
user1.add_balance(99999)
print(user1.show_balance())
