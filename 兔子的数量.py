def only(n):
    if n == 1:
        return 2
    elif n == 2:
        return 3
    else:
        return only(n-1)+only(n-2)
"""假设第一个月有2只，第二个月有3只，则第三个月有5只，每个月的数量等于这个月前两个月的兔子数量之和
1-2，2-3，3-5(2+3),4-(2+3)+3,5-(2+3)+3+2+3,6-(2+3)+3+2+3+(2+3)+3,7-"""
i=only(int(input()))
print(i)
#递归方法
