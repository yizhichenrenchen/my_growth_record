class object:
    pass
class Animal(object):
    pass
class Dog(Animal):
    pass
class Husky(Dog):
    pass
"""如上继承关系，object-->Animal-->Dog-->Husky,使用isinstance函数可以判断class的类型，例如
    a = Animal()
    b = Dog()
    c = Husky()
    然后判断isinstance(a,Animal)
    True
    isinstance(b,Dog)
    True
    isinstance(c,Husky)
    True
    由于继承关系，isinstance(c,Animal)结果也为True
    使用此方法也可判断一个变量是否是某些类型中的一种，例如
    """
isinstance([1,2,3],(list,tuple))#属于列表
isinstance((1,2,3),(list,tuple))#属于元组