"""动态规划实现"""

def climb_stairs(n:int)->int:
#边界条件处理，1阶时为1,2阶时为2
    if n <= 2:return n
    dp = [0]*(n+1)#创建长度为n+1的数组，因为n为索引，所以数组长度为n+1
    dp[1],dp[2] = 1,2#设定初始状态
    for i in range(3,n+1):#因为1和2已经设置好，所以从3开始循环
        dp[i] = dp[i-1]+dp[i-2]#核心递归函数
    return dp[n]

print(climb_stairs(1))
print(climb_stairs(2))
print(climb_stairs(5))
#空间优化后
def fib_d(n):
    a,b = 1,1
    for i in range(n):
        a,b = b,a+b
    return a
print(fib_d(5))