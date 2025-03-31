class Student:#创建学生类，包含姓名年龄属性
    def __init__(self,name,age):
        self.name = name
        self.age = age
    #创建显示信息方法
    def show_info(self):
        print(f"姓名{self.name},年龄{self.age}")

class Course:
    def __init__(self,name):
        self.course = name
        self.courses = []
    def enroll(self,course):
        self.courses.append(course)
cou=Course('高数')
stu=Student('李白')
