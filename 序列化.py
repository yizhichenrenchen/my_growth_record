#1.pickle模块
import pickle
d = dict(name = 'Bob',age = 20,score = 50)
print(pickle.dumps(d))
f = open('编程实验.txt','wb')
pickle.dump(d, f)
f.close()
#最好使用with语句管理文件，避免忘记关闭文件
with open('dump.txt','wb') as f:
    pickle.dump(d, f)
#反序列化
with open('dump.txt','rb') as f:
    d = pickle.load(f)
    print(d)
#json模块
import json
n = json.dumps(d)#dumps会把对象序列化成一个二进制东西
print(n)
#反序列化
b = json.loads(n)
print(b)
#进阶
#类序列化
class Student(object):
    def __init__(self,name,age,score):
        self.name = name
        self.age = age
        self.score = score

i = Student('Bob',22,20)
print(json.dumps(i.__dict__))
#ensure_ascii参数
obj = dict(name='小明',age = 20)
c = json.dumps(obj,ensure_ascii=False)
print(c)
h = json.dumps(obj,ensure_ascii=True)
print(h)
