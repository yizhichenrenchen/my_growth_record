#class开头，后面跟类名，通常大写开头例如：class Student
class Student(object):
    """可以通过在变量前加__实现变量私有化,私有变量外部无法访问，此时若想从外部获取私有变量，可以增加方法，通过方法访问,
    此时若还想在外部对变量进行修改的话，可以继续增加方法，这样做的好处是方法可以检查传入的参数，避免无效参数传入
    还有__name__此类变量，此类变量是可以直接访问的，若是变量名前只有一个下划线，虽然可以访问，但默认为私有变量
    从外部获取私有变量哈可以通过_Student__score的形式来进行访问，但是一般不这么做"""
    def __init__(self,name,score):
        self.name = name
        self.__score = score
    def get_score(self):
        if self.__score >= 90:
            return 'A'
        elif self.__score >= 70:
            return 'B'
        else:
            return 'C'
#定义好了类，即可根据类创建实例。例如
m = Student('李雷',95)
n = Student('韩梅梅',82)
#python允许对实例变量绑定任何数据，例如：
m.age = 21
n.age = 22
#通过实例变量直接调用方法，调用属性
print('姓名：'+m.name,'成绩等级：'+m.get_score(),'年龄：',m.age)
print(n.name,n.get_score(),n.age)

