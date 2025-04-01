#1.__slots__特殊变量
"""该变量可限制对类添加的属性，例如：
class Student:
     __slots__ = ('name','age')
    如此便可限制对类添加的属性，若尝试添加其他属性，则会报错"""
class Student:
    __slots__ = ('name','age')

s=Student()
s.name='lilei'
s.age=20
#s.score=66,此处score未在__slots__中，添加会报错
print(s.name,s.age)
#注意__slots__仅对当前类实例起作用，对继承其的子类不起作用，除非在子类中也添加__slots__，此时子类中可添加的属性为父类及子类__slots__中的属性
