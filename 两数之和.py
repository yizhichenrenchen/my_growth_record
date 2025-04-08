"""给定一个整数数组 nums 和一个整数目标值 target，请你在该数组中找出 和为目标
     值 target  的那 两个 整数，并返回它们的数组下标。"""
nums = input().split(',')
print(type(nums))
print(type(nums[0]))
list_nums=[int(x) for x in nums]
print(list_nums)
print(type(list_nums[0]))
"""target = int(input())
i=0
for nums[i] in nums:
    for nums[i+1] in nums:
        if nums[i]+nums[i+1] == target:
            print(nums[i], nums[i+1])
        i+=1"""





