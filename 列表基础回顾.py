#1.表示形式：
l1=[1,2,3,4,5,6,7]
l2=['lilei','hanmeimei']
#2.列表索引,注意索引越界会报错，范围为[-n~n)左开右闭，列表每个元素都可以是有效的数据类型，例如字符串，整数，列表等
print(l1[0],l2[0])
#3.长度获取
print(len(l1))
#4.元素可修改：(作为相似数据类型，字符串无法修改)
l2[0]='liubei'
#5.列表切片[start:end:step]分别代表起始索引，终止索引（不包含），步长，步长表示每隔几个元素进行取值
print(l1[0:5:2])
#6.列表运算符{==，！=，>,>=,<,<=}以及成员判断in，支持+和*
"""+代表列表拼接，*代表将列表元素进行翻倍并拼接，若*0则清空列表
==代表两个列表相等，长度相等且对应位置的元素也相等
!=代表两个列表不相等
>会从前向后对列表元素逐个判断，先判断到的对应位置元素大则大，>=则表示大于或者两个列表相等
小于和小于等于同理，但需要保证对应位置元素具有可比性，否则报错"""
#7.del关键字可用于列表，可删除对应索引元素或整个列表删除
#del l1[0]
#del l1
#8.在列表元素具有可比性的情况下，可通过max和min获取最大值或者最小值
#9.list()函数可用于强制转换为列表，例如,整数及浮点数无法转换，但整数可通过先转换为字符串，在转换为列表
l3 = list('python')
print(l3)
#10.sorted()函数，可用于对列表进行排序
#sorted(iterable,key=none,reverse=False或True)分别代表需要排序的对象，比较的内容，正序False或逆序True
l4 = [3,5,9,4,2,6,8,5,2,4,9]
print(sorted(l4,reverse=True))
#本函数并不会改变原来列表
#11.append()方法可用于对列表添加元素,将改变原列表
l4.append(25)
print(l4)
#12.pop()方法，此方法用于删除元素，从尾部删除，或者自定义索引,将改变原列表
l4.pop(6)
print(l4)
#13.insert()方法，此方法可对列表插入元素,将改变原列表
l4.insert(0,100)#表示从索引0的位置插入元素100
#14.index()方法，此方法可用于查找元素索引，返回第一个匹配到的元素索引位置，若元素不存在则会报错
print(l4.index(100))
#15.remove()方法，此方法可用删除元素，直接删除元素，并非索引位置，且查找不到该元素时报错
print(l4.remove(100))
#16.count()方法，此方法用于统计列表元素数量
print(l4.count(6))
#17.extend()方法，此方法可以实现列表拓展，在列表尾部追加其他序列的元素,将改变原列表
l4.extend(l3)
print(l4)
#18.reverse()方法，此方法可用于将列表翻转,将改变原列表
l4.reverse()
print(l4)
#19.sort()方法，此方法可通过reverse控制正序或逆序排列
l3.sort(reverse=True)
print(l3)








