class Employee:
    def __init__(self,name,salary,value):
        Employee.printclass(self,name,salary,'age',value)
        self.name = name
        self.salary = salary
    @classmethod
    def printclass(cls,obj,name,salary,age,value):
        if not hasattr(obj, age,):
            setattr(obj,age,value)
        else:
            print(f"{name}'s salary is {salary},his age is {age}")


name=input()
salary=int(input())
age=int(input())
e=Employee(name,salary,age)
e.printclass()