class Median:
    def __init__(self,nums1,nums2):
        self.nums1 = nums1
        self.nums2 = nums2
        self.nums3 = sorted(nums1+nums2,reverse=False)
    def mid(self):
        l=len(self.nums3)
        m=l//2
        if l%2==0:
            z=(self.nums3[m]+self.nums3[m-1])/2
            return "{:.5f}".format(z)
        else:
            e=(self.nums3[m])
            return "{:.5f}".format(e)
x=Median([1,3],[2])
print(x.mid())





