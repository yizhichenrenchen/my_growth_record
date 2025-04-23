"""斐波那契数 （通常用 F(n) 表示）形成的序列称为 斐波那契数列 。该数列由 0 和 1 开始，后面的每一项数字都是前面两项数字的和。也就是：

F(0) = 0，F(1) = 1
F(n) = F(n - 1) + F(n - 2)，其中 n > 1
给定 n ，请计算 F(n)"""
#递归实现
"""def fib(n):#此方法虽然代码简洁，但是计算时间长，大数不适合
    if n <= 1:
        return n
    return fib(n - 1) + fib(n - 2)


v = fib(123)
print(v)"""
#迭代实现,适合大数计算，计算fib(1000)也仅需1ms
def fib(n):
    a, b = 0, 1
    b = 0
    for i in range(n):
        a, b = b, a + b
        b+=1
    return b
print(fib(3))

#动态规划，更加降低时间复杂度
"""def fib_d(n,memo={}):
    if n <= 1:
        return n
    if n not in memo:
        memo[n] = fib_d(n-1,memo) + fib_d(n-2,memo)
    return memo[n]
v = fib_d(123)
print(v)"""


