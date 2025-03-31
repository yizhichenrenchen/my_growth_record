"""class Course:
    def __init__(self,name):#课程类课程名属性
        self.name = name

class Student:
    MIX_CREDIT=10
    def __init__(self,name):#学生类学生名属性
        self.name = name
        self.courses = []#储存选课
    def enroll(self,course):

        if len(self.courses)<3:#添加课程方法
            self.courses.append(course)#添加选课进选课记录中
            return True

        print('请注意选课已达上限！！！')#超过三门将提示
        return False






#创建实例
stu=Student('刘备')
cou=[Course(f"课程{i}") for i in range(3)]#通过列表推导式写出所选课程
for c in cou:
    stu.enroll(c)#将所选课程添加进课程记录，此处通过方法添加较为安全，若直接修改列表则比较危险
print(f"已选课程：{[c.name for c in stu.courses]}")#通过列表推导式表达选课，此处c.name表示对每个对象c访问其name属性"""


class Course:
    def __init__(self,name,credit):
        self.name = name
        self.credit = credit
class Student:
    MAX_CREDITS = 10
    def __init__(self,name):
        self.name = name
        self.courses = []#储存学分变量
    def enroll(self,course):
        total=sum(c.credit for c in course.courses)
        if total+course.credit <= self.MAX_CREDITS:
            self.courses.append(course)
            return True
        print('学分已达上限！！！')
        return False
    def total_credit(self):#计算总学分
        return sum(c.credit for c in self.courses)


