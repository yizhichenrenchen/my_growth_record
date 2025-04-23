"""给你一个整数 x ，如果 x 是一个回文整数，返回 true ；否则，返回 false 。

回文数是指正序（从左向右）和倒序（从右向左）读都是一样的整数。

例如，121 是回文，而 123 不是"""
class Palindrome(object):
    def __init__(self,number):
        self.number = number
    def string(self):
        return str(self.number)

    def reverses(self):
        return self.string()[::-1]

    def ints(self):
        i1 = self.reverses()
        try:
            return int(i1)
        except ValueError:
            return None
    def judg(self):
        if self.number < 0:
            return False
        i5 = self.ints()
        if i5 is None:
            return False
        else:
            return self.number == i5



int1 = Palindrome(input())


print(int1.judg())

"""总结：调用方法需要加括号，例如self.reverses()才能调用成功，比较方法返回值而非对象，注意
   在ints中需要加入异常处理来处理负数输入"""




