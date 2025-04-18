"""给你一个 32 位的有符号整数 x ，返回将 x 中的数字部分反转后的结果。

如果反转后整数超过 32 位的有符号整数的范围 [−231,  231 − 1] ，就返回 0。

假设环境不允许存储 64 位整数（有符号或无符号）"""
"""x = input()

if -2**31 <= int(x) <= 2**31-1:


    if x[0] =='-':
        print(-int(x[1:][::-1]))
    else:
        print(int(x[::-1]))
else:
    print(0)"""


class Turn:
    def __init__(self,x:int):
        self.x = str(x)
        self.reverse_num = 0
    def reverse(self):
        if int(self.x) < 0:
            s = -int(self.x[1:][::-1])
            return s
        else:
            g = int(self.x[::-1])
            return g
    def validate_range(self):
        try:
            self.reverse_num = self.reverse()
            return -2**31 <= self.reverse_num <= 2**31-1
        except ValueError:
            return "数字超过范围"
    def values(self):
        if self.validate_range():
            return self.reverse_num
        else:
            return 0
v = Turn(120)
print(v.values())






"""    def turn(self):
        if -2**31 <= int(self.x) <= 2**31-1:
            if int(self.x) < 0:
                l = -int(self.x[1:][::-1])
                return l
            else:

                k = int(self.x[::-1])
                return k
        else:
            return 0

n = Turn(0)
print(n.turn())"""






