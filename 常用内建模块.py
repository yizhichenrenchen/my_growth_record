#1.获取日期和时间
from datetime import datetime
now = datetime.now()
print(now)
#要指定某个时间，可以构造一个时间
dt = datetime(2015,9,15,12,32,21)
print(dt)
#转换为timestamp
print(dt.timestamp())
#timestamp转换为datetime需要使用fromtimestamp()方法：
n = 1442291541.0
print(datetime.fromtimestamp(n))
#字符串转换为日期时间
l = datetime.strptime('2001-5-19 15:21:34', '%Y-%m-%d %H:%M:%S')#注意Y大写以及需要格式化的格式
print(l)
#转化为字符串
b = datetime.now()
print(b.strftime( '%Y-%m-%d %H:%M:%S'))
#时间计算
from datetime import timedelta,datetime
v = datetime.now()
print(v)

print(v+timedelta(hours=6))
print(v-timedelta(hours=6))
print(v+timedelta(days=2,hours=10))



