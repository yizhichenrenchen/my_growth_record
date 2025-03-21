#基类，定义账户，余额，以及存款，取款等方法
"""父类定义账户owner，存款方法deposit，取款方法withdraw，账户及余额显示，余额获取
利率子类通过继承父类存款方法将利润存进余额，新增参数利率super（）调用父类方法
取款手续费子类通过继承父类取款方法，并且重写父类方法获得手续费，再调用父类取款方法将手续费及取款金额一同取出
"""


class Bankaccount:
    def __init__(self,owner,balance):#两个参数：户名，余额
        self.owner=owner
        self.__balance=balance#私有属性
    #存款
    def deposit(self,amount):#存款方法，一个参数，存入多少钱
        if amount > 0:
            self.__balance+=amount
            print(f"存入{amount}元，余额为{self.__balance}")
            return True
        else:
            print("存入数量需大于0，请重新操作，谢谢")
            return False
    def withdraw(self,amount):
        if 0 < amount <= self.__balance:
            self.__balance-=amount
            print(f"取出{amount}元，您的余额为{self.__balance}")
            return True
        else:
            print("您的余额不足或取款数量错误，请重新输入")
            return False
    def display_balance(self):
        """显示余额"""
        print(f"账户持有人{self.owner},余额{self.__balance}")
    def get_balance(self):
        return self.__balance#获取余额，避免直接访问私有属性
#储蓄账户，新增利率，继承普通账户
class SavingsAccount(Bankaccount):
    def __init__ (self,owner,balance,interest_rate=0.03):#新加入参数：利率
        super().__init__(owner,balance)
        self.__interest_rate = interest_rate
    def add_interest(self):
        interest=self._Bankaccount__balance*self.__interest_rate#计算利率
        self.deposit(interest)#复用父类方法
class CheckingAccount(Bankaccount):
    def __init__(self,owner,balance,fee=0.01):
        super().__init__(owner,balance)
        self.fee = fee#新增手续费参数
        self.fee_history=[]#记录手续费历史



    def withdraw(self,amount):

        total = self.fee*amount+amount#重写父类方法
        if super().withdraw(total):#调用父类方法取款
            print(f"手续费{self.fee*amount},实际取款金额{amount}")
            self.fee_history.append(self.fee)
            return True
        else:
            print(f"取款失败，手续费{self.fee*amount}+取款金额{amount}超过余额")
            return False









if __name__=='__main__':
    account1 = Bankaccount('陈文博',1000)
    account1.deposit(500)
    account1.withdraw(200)
    account1.display_balance()


    Savings=SavingsAccount('陈文博',3000,0.02)
    Savings.add_interest()
    Savings.display_balance()


    checking=CheckingAccount('陈文博',200)
    checking.withdraw(100)
    checking.display_balance()








