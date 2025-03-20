#基类，定义账户，余额，以及存款，取款等方法
class Bankaccount:
    def __init__(self,owner,balance):#两个参数：户名，余额
        self.owner=owner
        self.__balance=balance#私有属性
    #存款
    def deposit(self,amount):#存款方法，一个参数，存入多少钱
        if amount > 0:
            self.__balance+=amount
            print(f"存入{amount}元，余额为{self.__balance}")
        else:
            print("存入数量需大于0，请重新操作，谢谢")
    def withdraw(self,amount):
        if 0 < amount <= self.__balance:
            self.__balance-=amount
            print(f"取出{amount}元，您的余额为{self.__balance}")
        else:
            print("您的余额不足或取款数量错误，请重新输入")
    def display_balance(self):
        """显示余额"""
        print(f"账户持有人{self.owner},余额{self.__balance}")
#储蓄账户，新增利率，继承普通账户
class SavingsAccount(Bankaccount):
    def __init__ (self,owner,balance,interest_rate=0.03):#新加入参数：利率
        super().__init__(owner,balance)
        self.__interest_rate = interest_rate
    def add_interest(self):
        interest=self._Bankaccount__balance*self.__interest_rate#计算利率
        self.deposit(interest)#复用父类方法
class CheckingAccount(Bankaccount):
    def __init__(self,owner,balance,handling_fee=0.01):
        super().__init__(owner,balance)

        self.__handling_fee = handling_fee
    def withdraw(self,amount):
        super().withdraw(amount)
        handling_fee=amount*self.__handling_fee
        self.withdraw(handling_fee)







if __name__=='__main__':
    account1 = Bankaccount('陈文博',1000)
    account1.deposit(500)
    account1.withdraw(200)
    account1.display_balance()


    Savings=SavingsAccount('陈文博',3000,0.02)
    Savings.add_interest()
    Savings.display_balance()

    handling=CheckingAccount('陈文博',3000)
    handling.withdraw(600)
    handling.display_balance()






