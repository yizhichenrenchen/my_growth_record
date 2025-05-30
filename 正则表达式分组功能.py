#用括号就是表示要提取的分组比如^(\d{3})-(\d(5,8})$,可以直接从匹配的字符串中提取出区号和本地号码
import re
m = re.match(r'^(\d{3})-(\d{3,8})$','010-12345')
print(m)
print(m.group(0))
print(m.group(1))
print(m.group(2))
#group(0)是与整个正则表示相匹配的字符串，group(1），group(2)......分别表示第1,2......个子串
#提取子串之时间匹配
t = '19:05:30'
n = re.match(r'^(0[0-9]|1[0-9]|2[0-3]|[0-9])\:(0[0-9]|1[0-9]|2[0-9]|3[0-2]|4[0-9]|5[0-9]|[0-9])\:(0[0-9]|1[0-9]|2[0-9]|3[0-9]|4[0-9]|5[0-9]|[0-9])$',t)
print(n.groups())#这表达式直接识别合法的时间，但是无法识别日期
#正则表达式默认贪婪匹配,例如匹配数字0
p = re.match(r'^(\d+)(0*)$','102300')
print(p.groups())#此时因为是贪婪匹配模式，会匹配最后一个0后面
p1 = re.match(r'^(\d+?)(0*)$','20010915000')
print(p1.groups())
#如果一个正则表达式要使用多次，出于效率考虑，可以提前进行编译正则表达式，接下来使用时将跳过编译步骤
p2 = re.compile(r'^(\d{3})-(\d{3,8})$')#后面可直接使用
print(p2.match('010-12345').groups())
print(p2.match('010-8086').groups())