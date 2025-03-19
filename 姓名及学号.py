my_dict_1={'name':'Niuniu','Student ID':1}
my_dict_2={'name':'Niumei','Student ID':2}
my_dict_3={'name':'Niu Ke Le','Student ID':3}
dict_list=[]
dict_list.append(my_dict_1)
dict_list.append(my_dict_2)
dict_list.append(my_dict_3)
for i in dict_list:
    print("{}'s student id is {}".format(i['name'],i['Student ID']))
#format格式化操作---{}----{}----.format(参数1，参数2)
