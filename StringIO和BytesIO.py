#一.StringIO
from io import StringIO
f = StringIO()
f.write('hello')
f.write(' ')
f.write('world')
print(f.getvalue())
#getvalue用于获取写入后的str
#要读取StringIO,可以用一个str初始化一个StringIO，然后，像读文件一样读取：
m = StringIO('hello\nHi\nworld!')
while True:
    s= m.readline()
    if s == '':
        break
    print(s.strip())
#二.BytesIO
#StringIO只能操作str，要想操作二进制数据，就必须使用BytesIO
#BytesIO实现了在内存中读取bytes，创建一个BytesIO，然后写入一些东西
from io import BytesIO
i = BytesIO()
i.write('中文'.encode('utf-8'))
print(i.getvalue())
#同理，可以用一个bytes初始化BytesIO，然后，像读文件一样读取
p  = BytesIO(b'\xe4\xb8\xad\xe6\x96\x87')
print(p.read())

