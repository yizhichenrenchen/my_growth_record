class Employee:
    def __init__(self,name,salary) -> None:
        self.name=name
        self.salary=salary

    def printclass(self):
        try:#错误捕捉
           print(f"{self.name}'salary is {self.salary}, and his age is {self.age}")
        except AttributeError:
            print("Error! No age")


name=input()
salary=int(input())
age=int(input())

e=Employee(name,salary)
e.printclass()
e.age=age#直接在实例中添加属性
e.printclass()



