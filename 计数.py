
j=list(map(int,input().split()))
i=j.count(0)
print(i)
#此处引申出map函数用法，上面为将列表元素字符串转换为整数
#还可以用来数学运算，结合匿名函数
nums = [1,2,3,4,5,6,7,8,9]
l=list(map(lambda x:x**2,nums))
print(l)