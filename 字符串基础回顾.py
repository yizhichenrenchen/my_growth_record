#一.大小写转换：
#1.lower()该方法可以将字符串全部转换为小写，不会改变元字符串
s1 = 'I love Python'
s2 = s1.lower()
print(s2)
print(s1)
#2.upper()方法，该方法可以将字符串字符转化为大写字母,不会改变原字符串
s3 = 'hello world'
s4 = s3.upper()
print(s4)
print(s3)
#3.title()方法，此方法可以将字符串每个独立单词首字母大写，运行原理为先将字符串中非字母字符转换为空格之后，此时每个分离的单词首字母大写，不会改变原字符串
s5 = 'i love ch1ina'#会将1先转化为空格，此时ina也是一个独立的单词
s6 = s5.title()
print(s6)
print(s5)
#4.capitalize()方法，此方法可以将字符串首字符大写，不会改变原字符串
s7 = 'i Love Python'
s8 = s7.capitalize()
print(s8)
print(s7)
#5.swapcase()此方法可以实现字符串字符大小写互相转换
s9 = 'i Love Python'
s10 = s9.swapcase()
print(s10)
print(s9)
#二.字符判断
#1.isalnum()方法，此方法可以判断字符串的所有字符是否都是数字或字母，此方法返回True或False
a1 = '123python'
a2 = '123,python'
print(a1.isalnum())
print(a2.isalnum())
#2.isalpha()方法，此方法可以判断字符串是否都是字母
a3 = 'hello,world'
a4 = 'python'
print(a3.isalpha())
print(a4.isalpha())
#3.isdigit()方法，此方法可以判断字符是否都是二进制数字(0~9),或者角标类型阿拉伯数字
a5 = '20010519'
a6 = '2001.0915'
print(a5.isdigit())
print(a6.isdigit())
#角标类型：只需关注是不是阿拉伯数字，不关注位置，角标也符合条件
#4.isdecimal()此方法可以判断所有字符是不是都是十进制数字或者以10为底的十进制数
#5.isnumeric()此方法可以判断所有字符是不是都是数字，此方法还可以判断罗马数字，以及分数，此方法判断字符的所有Unicode值
a7 = '123'
a8 = '贰'
print(a7.isnumeric())
print(a8.isnumeric())
#7.islower()方法，此方法判断字符是不是都是小写字母
a9 = 'i love python'
a10 = 'i love Python'
print(a9.islower())
print(a10.islower())
#8.isupper()判断是否都是大写字符
a11 = 'python'
a12 = 'PYTHON'
print(a11.isupper())
print(a12.isupper())
#9.istitle()，此方法可以判断首字符是否大写
a13 = 'I Love Ch1ina'
a14 = 'I Love Python'
print(a13.istitle())
print(a14.istitle())
#10.isspace()方法，此方法可以判断是否都是空白字符，包括空格，\n换行符，\t(水平制表符),\r(回车)
a15 = '     '
a16 = '    \n'
a17 = '     \r'
print(a15.isspace())
print(a16.isspace())
print(a17.isspace())
#三.格式控制
#1.center(width,fillchar='')方法，此方法可以实现字符串居中排列可以指定填充字符，默认空格
z1 = 'hello'
z2= z1.center(10,'*')
print(z2)
#2.ljust(width,fillchar='')此方法可以实现左对齐
z3 = 'hello'
z4 = z3.ljust(10,'*')
print(z4)
#3.同理右对齐rjust(width,fillchar='')
z5 = 'hello'
z6 = z5.rjust(10,'*')
print(z6)
#4.format,格式化字符串
z7 = "{}&{}".format('chenwenbo','huxiaoya')
print(z7)
#从左至右依次填充，也可控制
z8 = "{0}*{1}*{0}".format('chenwenbo','huxiaoya')#此处0和1分表代表字符索引位置
print(z8)
#也可通过指定名称
z9 = "网站名：{name},网址：{url}".format(name='xiaoqikeji',url='xiaoqi.com')#通过字典实现数据填充
print(z9)
#对于int和float类型，还可以通过：额外控制
z10 = "{:.4f}".format(3.14)
print(z10)
#还可以实现对齐操作
print("{:>10f}".format(3.14))#右对齐
print("{:<10f}".format(3.14))#左对齐
print("{:^10f}".format(3.14))#居中对齐
#填充对齐
print("{:0>10f}".format(3.14))#右对齐
print("{:0<10f}".format(3.14))#左对齐
print("{:0^10f}".format(3.14))#居中对齐
#四，空白删除
#1.lstrip()方法,此方法可以删除字符串左侧的空白
x1 = '    my name is chenwenbo'
x2 = x1.lstrip()
print(x2)
#2.同理rstrip()方法可以删除字符串右侧的连续空白
x3 = '  python       '
x4 = x3.rstrip()
print(x4)
#3.strip()方法可以删除左侧和右侧的连续空白
x5 = '    python     '
x6 = x5.strip()
print(x6)
#此方法除了可以删除空格，还可以删除首尾指定的字符
x7 = 'hello,world,hello'
x8 = x7.strip('hello')
print(x8)
#五.字符串替换
#replace()方法
c1 = 'hello'
c2 = c1.replace('e','0')
print(c2)
#六.字符串连接
#join()方法
c3 = 'i'
c4 = 'love'
c5 = 'python'
print(' '.join([c3,c4,c5]))
#七.字符串查找
#1.find()方法，该方法回从前往后进行匹配，若未查找到则返回-1，否则返回该字符首次出现的位置索引
v1 = 'hello,world'
print(v1.find('l'))
print(v1.find('python'))
#2.index()方法，此方法与find较为类似，只是不存在时会抛出异常
v2 = 'hello,world'
print(v2.index('l'))
try:
    print(v2.index('python'))
except ValueError:
    print('value error')
#3.rfind()方法，此方法用于检测是否包含指定的子字符串，若未检测到返回-1，否则返回最后一次出现该子字符串的位置索引
v3 = 'hello,world'
print(v3.rfind('l'))
print(v3.rfind('python'))
#4.rindex()方法，同理，此方法会返回最后一次匹配的索引位置，若未检测到则抛出异常
#八.字符串计数
#count()方法
d1 = 'hello,world'
print(d1.count('l'))
#九.字符串分割
#split(sep=None, maxsplit=-1)
#其中sep指定我们用于分割的字符。如果不指定，则默认使用空白字符进行分割。maxsplit指定我们最多使用分割符的次数,默认为-1，表示不限制次数
d2 = 'hello,world'
print(d2.split())
print(d2.split('l'))
print(d2.split('l',1))