"""用@property给对象加上width和height属性，以及一个只读属性resolution
@property装饰器将方法转换为属性调用，注意属性前下划线"""



class Screen:

    @property#读
    def width(self):
        return self._width
    @width.setter#写
    def width(self,value):
        self._width = value
    @property#读
    def height(self):
        return self._height
    @height.setter#写
    def height(self,value):
        self._height = value
    @property#读，该属性因为只有读，没有写，所以为只读属性
    def resolution(self):
        return self._width*self._height
#测试
s = Screen()
s.width = 1024
s.height = 768
print('resolution=',s.resolution)
if s.resolution == 786432:
    print('ok')
else:
    print('error')