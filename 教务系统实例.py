"""本例通过两个父类分别定义学生系统和课程系统，学生系统包括学号，姓名，以及学生选课记录变量，课程类包括课程ID，
课程名称，学分以及选课容量属性和初始化为0的当前选课人数，在通过Enrollment类将课程系统和学生系统关联，并且在此类中
通过@classmethon定义类方法用来判断课程容量是否还可选，在__init__下面先进行判断是否可选，然后在操作实例属性
此类中还有类变量all_enrollments用来储存全局选课记录，类变量通常用来记录全局变量，本例中即为记录全局选课记录，通过append方法
将选课情况添加进对应变量中，"""




class Student:#学生类，无类变量
    def __init__(self, student_id: str, name: str):#两个参数，学号，姓名
        self.student_id = student_id#实例属性
        self.name = name#实例属性
        self.enrolled_courses = []  # 存储选课记录对象


class Course:#课程类，定义课程的基本属性
    def __init__(self, course_id: str, name: str, credit: int, capacity: int):
        self.course_id = course_id#课程编号，实例属性
        self.name = name#课程名称，实例属性
        self.credit = credit#学分，实例属性
        self.capacity = capacity#最大容量通过最大容量和当前选课人数实现选课人数控制，实例属性
        self.current_students = 0#当前选课人数


class Enrollment:
    all_enrollments = []#记录全局选课记录，类变量，储存类级别的公共数据，例如统计实例数量，本类变量为储存全局选课记录这个统计过的实例数量

    def __init__(self, student: Student, course: Course):#关联属性
        if self.check_availability(course):#调用类方法检查课程容量
            self.student = student#关联学生,实例属性
            self.course = course#关联课程类，实例属性
            self.grade = None#初始化成绩
            student.enrolled_courses.append(self)#更新选课列表
            course.current_students += 1#更新选课人数
            Enrollment.all_enrollments.append(self)#更新全局选课记录

    @classmethod#将方法绑定到类
    def check_availability(cls, course):#将方法绑定到类
        return course.current_students < course.capacity#返回判断选课结果的值，但此处只返回成功结果，失败默认返回none


class Grade:
    @staticmethod
    def enter_grade(enrollment: Enrollment, score: float):
        if 0 <= score <= 100:
            enrollment.grade = score
            return True
        return False