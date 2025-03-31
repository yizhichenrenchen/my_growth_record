#1.在实例中操作属性

class Student:
    def __init__(self,name,score):
        self.name = name
        self.score = score
    def add_age(self,age):#此方法用来对对象进行动态检查，修改


        if not hasattr(self, 'age'):#判断有无该属性
            setattr(self,'age',age)#若没有，则添加，注意属性名需要引号，且后面需要跟新属性的值
            print(f'已添加属性：{age}')
        else:
            print(f'已有age属性：{getattr(self, "age")}')
p=Student('lilei',20)
p.add_age(10)#添加age属性
p.add_age(20)#已添加属性，返回已有该属性以及值
#2.在类方法中操作
class Config:
    default_theme = "light"

    @classmethod
    def check_and_set_theme(cls, theme):
        # 检查类是否有 'default_theme' 属性
        if hasattr(cls, 'default_theme'):#判断有无属性default_theme，若没有，则添加并且设置值为theme
            setattr(cls, 'default_theme', theme)
            print(f"修改类属性 default_theme 为: {theme}")
        else:
            print("类属性 default_theme 不存在")

# 使用
Config.check_and_set_theme("dark")  # 输出: 修改类属性 default_theme 为: dark
#3.在__init__构造函数中可用来动态初始化实例属性
class DynamicObject:
    def __init__(self, **kwargs):
        # 动态添加所有传入的属性
        for key, value in kwargs.items():
            setattr(self, key, value)

# 使用
obj = DynamicObject(name="Alice", age=30)
print(obj.name)  # 输出: Alice
print(hasattr(obj, 'age'))  # 输出: True