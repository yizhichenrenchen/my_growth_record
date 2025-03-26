class Employee:
    def __init__(self,name,salary,age_value):

        self.name = name
        self.salary = salary
        has_age = hasattr(self,'age')#hasattr判断有无参数，注意该参数要用引号
        print(has_age)#直接打印判断结果
        if not has_age:#not False即为True，运行下面添加步骤

            setattr(self,'age',age_value)#添加该参数并将传入的参数作为age的值，注意参数要用引号
        self.printclass()#调用打印方法

    def printclass(self):#打印方法

            print(f"{self.name}'s salary is {self.salary},his age is {self.age}")


name=input()
salary=int(input())
age=int(input())
e=Employee(name,salary,age)#创建实例e



