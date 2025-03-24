p=input()#输入字符串
l=list(p)#转化为列表

m=dict()#初始化空字典
for i in l:#循环列表元素
    m.setdefault(i,0)#向字典添加键值对并让值为0
    if i in m:#判断键是否已经被添加进字典中，若是，则值+1
        m[i]+=1
    else:#否则值为1
        m[i]=1
print(m)
