"""给实例绑定属性的方法是通过实例变量，或者
通过self变量，如果要给类绑定一个属性，可以在类中直接定义变量，当定义了
类属性后，归类所有，但所有实例也可以访问"""
#下面通过一个例子来说明
"""创建一个学生类，创建一个类属性，每创建一个实例
，该属性自动增加"""
class Student:
    count = 0
    def __init__(self,name):
        self.name = name
        Student.count += 1#来自网友的一句话：为什么要在构造函数下面写Student.count += 1？ 因为每当创建一个新的类实例时，构造函数就会被自动调用，而因为Student.count += 1在构造函数里面，所以也会被激活，从而实现一次累加，如此反复，就能“检测“出创建了多少实例了
if Student.count != 0:
    print('测试失败')
else:
    bart=Student('bart')
    if Student.count != 1:
        print('测试失败')
    else:
        lisa=Student('lisa')
        if Student.count != 2:
            print('测试失败')
        else:
            print('Students:',Student.count)
            print('测试通过')