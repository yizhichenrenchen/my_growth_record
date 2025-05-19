"""假设你是一位很棒的家长，想要给你的孩子们一些小饼干。但是，每个孩子最多只能给一块饼干。
对每个孩子 i，都有一个胃口值 g[i]，这是能让孩子们满足胃口的饼干的最小尺寸；并且每块饼干 j，都有
一个尺寸 s[j] 。如果 s[j] >= g[i]，我们可以将这个饼干 j 分配给孩子 i ，这个孩子会得到满足。你的目标是满足尽可能
多的孩子，并输出这个最大数值。"""
class distribution:
    def __init__(self,appetite:list,size:list):
        self.appetite=sorted(appetite)
        self.size=sorted(size)

        self.max_v = 0
    def dist(self):
        i = j = 0
        while i<len(self.appetite) and j<len(self.size):
            if self.size[j] >= self.appetite[i]:
                self.max_v += 1
                i+=1
            j+=1



    def results(self):
        return self.max_v

dis1 =distribution([1,2,3],[1,1])
dis1.dist()
print(dis1.results())




