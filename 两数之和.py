"""给定一个整数数组 nums 和一个整数目标值 target，请你在该数组中找出 和为目标
     值 target  的那 两个 整数，并返回它们的数组下标。"""

#print(type(nums)),字符串
#print(type(nums[0]))字符串
#list_nums=[int(x) for x in nums]列表推导式转化为列表的同时将元素转化为整数，可优化为：
nums = input().replace('[','').replace(']','').replace(' ','')
#print(nums)
#print(type(nums[0]))
list_nums=list(map(int,nums.split(',')))
#print(list_nums)
#(type(list_nums[0]))
target = int(input())
for i in range(len(list_nums)):#变量i代表从0到列表长度的数组范围中遍历的某个数，实际上生成一个可以遍历的数组
    for j in range(i+1,len(list_nums)):#变量j代表从i+1到列表长度的数组范围中便利的某个数
        if list_nums[i] + list_nums[j] == target:#此处精髓所在，让i下标代表的数和j下标代表的数相加而不是i和j直接相加
            print(f'[{i}, {j}]')
            exit()#此处如果有结果直接退出
"""知识点总结：
1,通过replace方法可以将字符串中多余的字符替换掉
2，通过map函数构造列表
3，不着急直接遍历列表，而是将遍历范围先转化为实际上由下标组成的数组，再遍历下标，在if条件中在用索引计算对应位置数字
4，exit（）退出循环"""





