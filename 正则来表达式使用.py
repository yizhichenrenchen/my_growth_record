import re
test = '010-22581'
if re.match(r'^\d{3}\-\d{5,8}$', test):
    print('OK')
else:
    print('ERROR')
#还可以使用正则表达式来分割字符串，例如
m = 'a b   c'.split(' ')
print(m)#此时连续多个空格分开识别
n = re.split(r'\s+','a b   c')
print(n)#可以识别连续多个空格
#用正则表达式分个字符极为方便，可以识别多个字符，如归输入一组标签，可以把不规范的输入转化为正确的字符
#验证邮箱地址是否合法
e  =input('请输入您的邮箱地址：')
if re.match(r'^\w+\.?\w+@[\w|\d]+.com',e):#此处正则表达式表示开头至少一个字母或数字+最多一个符号+@+数字或字母+.com
    print('OK')
else:
    print('ERROR')