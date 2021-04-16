class Bank:
    bname='sbi'        #static variable
    def acCreate(self,acno,name):
        self.acno=acno
        self.name=name
        self.minimumbal=5000
        self.balance = self.minimumbal

    def deposit(self,amt):
        self.balance += amt
        print("your",Bank.bname,"account has been credited with amt",amt)# static variable is called using class name
        print("your currrent balance=", self.balance)

    def withdrw(self,amt):
        if amt > self.balance:
            print("insufficient balance")
        else:
            print("account debited with",amt)
            self.balance-=amt
            print("available balance", self.balance)
obj = Bank()
obj.acCreate(123, 'abc')
obj.deposit(2500)
obj.withdrw(1000)
