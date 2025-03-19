result_dict={'Allen':['red','blue','yellow'],'Tom':['grean','white','blue'],'Andy':['black','pink']}
sort_result_dict=sorted(result_dict)#排序

for name in sort_result_dict:
    print("{}'s favorite colors are:".format(name))
    for favorite in result_dict[name]:
        print(favorite)
"""第一次遍历键，第二次遍历键对应的值的列表"""