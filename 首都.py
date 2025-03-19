cities_dict={'Beijing':{'Capital':'China'},'Moscow':{'Capital':'Russia'},'Paris':{'Capital':'France'}}
sorted(cities_dict.keys())

for city in cities_dict:#遍历键
    for i,j in cities_dict[city].items():#两个参数分别遍历值的键和值

        print('{} is the {} of {}!'.format(city,i.lower(),j))
"""涉及items应用，items()可以返回键值元组"""