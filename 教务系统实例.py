class Student:#学生类
    def __init__(self, student_id: str, name: str):#两个参数，学号，姓名
        self.student_id = student_id#实例属性
        self.name = name#实例属性
        self.enrolled_courses = []  # 存储选课记录对象


class Course:#课程类，定义课程的基本属性
    def __init__(self, course_id: str, name: str, credit: int, capacity: int):
        self.course_id = course_id#课程编号
        self.name = name#课程名称
        self.credit = credit#学分
        self.capacity = capacity#最大容量通过最大容量和当前选课人数实现选课人数控制
        self.current_students = 0#当前选课人数


class Enrollment:
    all_enrollments = []#记录全局选课记录

    def __init__(self, student: Student, course: Course):#关联属性
        if self.check_availability(course):#调用类方法检查课程容量
            self.student = student#关联学生
            self.course = course#关联课程类
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