"""字符串轮转。给定两个字符串s1和s2，请编写代码检查s2是否为s1旋转而成（比如，waterbottle是erbottlewat旋转后的字符串）"""
class rotation(object):
    def __init__(self,s1,s2):
        self.s1 = s1
        self.s2 = s2
        self.l = []
    def rotate(self):
        self.l = []
        for i in range(1,len(self.s2)):
            m = self.s2[i::]+self.s2[0:i:]
            self.l.append(m)
        return self.l
    def judgment(self):
        if len(self.s1) != len(self.s2):
            return False
        if self.s1 == self.s2:
            return True
        if self.s1 in self.l:
            return True
        else:
            return False

n = rotation('a','a')

print(n.judgment())










