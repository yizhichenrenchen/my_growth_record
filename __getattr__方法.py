#__getattr__
"""此方法可以在我们调用不存在的类的属性或方法时，在getattr方法中尝试获取属性，这样，
有机会返回需要得值，例如"""
class Student(object):
    def __init__(self,name):
        self.name = 'lilei'
    def __getattr__(self,attr):
        if attr == 'score':
            return 99
s=Student('lilei')
print(s.name)
print(s.score)#此处调用虽然Student类中虽然有score属性，但__getattr__方法中有该属性，此方法若在类中没有搜索到该属性，则会在此方法中进行搜索，若是类中已有该属性，则不会再该方法中搜索
#此方法可实现完全动态调用
"""class Chain(object):
    def __init__(self,path=''):
        self._path = path

    def __getattr__(self,path):
        return Chain('%s/%s'%(self._path,path))
    def __str__(self):
        return self._path
    __repr__ = __str__
path1 = Chain().status.user.timeline.list#此处是通过连续访问生成路径，通过每次触发__getattr__来添加路径
print(path1)"""
#通过callable()函数可以判断一个对象能否被调用，例如
print(callable(max))#输出True
#若要实现路径中动态参数替换，例如将用户名替换，可以通过改写__getattr__方法实现，或者在类中添加__call__方法，如下
class Chain(object):
    def __init__(self,path=''):
        self._path = path

    def __getattr__(self,name):
        return Chain(f'{self._path}/{name}')
    def __call__(self,param):
        return Chain(f'{self._path}/{param}')
    def __str__(self):
        return self._path
    __repr__ = __str__
path1 = Chain().users('michale').repos
print(path1)

