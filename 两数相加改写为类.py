class Add(object):
    def __init__(self,nums1,nums2):
        self.nums1 = nums1[::-1]
        self.nums2 = nums2[::-1]
    def num1(self):
        total1 = 0
        for i in range(len(self.nums1)):
            total1 += self.nums1[i] * 10 ** i

        return total1
    def num2(self):
        total2 = 0
        for i in range(len(self.nums2)):
            total2 += self.nums2[i]*10**i

        return total2
    def add(self):
        a = self.num1()+self.num2()
        if a == 0:
            return [0]
        b = [int(f) for f in str(a)]
        return b[::-1]


adder = Add([2,4,3],[5,6,4])
print(adder.num1())
print(adder.num2())
print(adder.add())



