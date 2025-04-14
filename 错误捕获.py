#1.try....except....方法
try:
    m = 10/0#可能出现错误的语句
except ZeroDivisionError:
    print('不能除以0！')
#2.捕获多个错误
try:
    a = int('abc')
except ValueError:
    print('ValueError')#值错误
except TypeError:
    print('TypeError')#类型错误
#上述方法也可改为合并捕获
try:
    pass
except (ValueError,TypeError) as e:
    print(e)
#3.捕获所有异常（不推荐使用）
try:
    pass
except Exception as e:
    print(e)
#4.else语句，跟在try...except...语句后面，无异常时将要执行的语句
try:
    pass
except Exception as e:
    print(e)
else:
    pass
#5.finally，同样跟在try...except...语句后面，不管有无异常都执行的语句，通常用来清理资源
try:
    file = open('test.txt','w')
except FileNotFoundError as e:
    print(e)
finally:
    print('清理资源')
    file.close()
#6.raise,主动抛出异常,触发条件直接抛出异常
def Check_age(age):
    if age < 0:
        raise ValueError('年龄不能为负数')
    return age
try:
    Check_age(-6)
except ValueError as e:
    print(e)
#7.自定义异常，继承Exception
class MyCustomError(Exception):
    def __init__(self,message):
        super().__init__(message)
try:
    raise MyCustomError('自定义错误信息')
except MyCustomError as e:
    print(e)
#8.assert,断言，用于调试，条件为假时触发
def divide(a,b):
    assert b!=0,'被除数不能为0'#当b=0时断言成功，输出错误语句
    return a/b
divide(10,0)#此时的调用b=0，断言成功
#9.上下文管理器(with)
try:
    with open('test.txt','r') as f:
        content = f.readlines()
except FileNotFoundError :
    print('文件不存在')
#10.记录错误日志(logging)
import logging
logging.basicConfig(filename='test.log',level=logging.DEBUG)

try:
    1/0
except ZeroDivisionError as e:
    logging.error('发生除零错误：%s',e,exc_info=True)
