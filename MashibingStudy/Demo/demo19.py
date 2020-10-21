# 作者：季毛毛
# 日期：2020/10/14 18:00
# 作用：字典

'''字典的创建方式'''
'''使用{}创建字典'''
score={'zhangsan':100,'lisi':98,'wangwu':45}
print(score)
'''使用dict()'''
student=dict(name='jack',age=20)
print(student)

'''获取字典的元素'''
score={'zhangsan':100,'lisi':98,'wangwu':45}
print(score['zhangsan'])
'''使用get获取元素'''
print(score.get('zhangsan'))
'''两者的区别,查找失败时：'''
#print(score['chenliu'])#报错
print(score.get('chenliu'))#输出none
'''查找不存在时，可以设置默认值'''
print(score.get('maqi',200))

'''key的判断'''
score={'zhangsan':100,'lisi':98,'wangwu':45}
print('zhangsan' in score)

'''删除'''
del score['zhangsan']#删除指定key
print(score)
score.clear()#清空
print(score)

'''添加元素，等同于修改'''
score['chenliu']=55#添加
print(score)
score['chenliu']=555#修改
print(score)

'''获取字典视图'''
'''获取所有的key'''
score={'zhangsan':100,'lisi':98,'wangwu':45}
keys=score.keys()
print(keys,type(keys))
print(list(keys))#将所有的key组成的视图转成列表
'''获取所有的value'''
values=score.values()
print(values,type(values))
print(list(values))
'''获取所有的key-value对'''
item=score.items()
print(item)
print(list(item))#转换之后的元素是由元组构成

'''字典元素的遍历'''
score={'zhangsan':100,'lisi':98,'wangwu':45}
for item in score:
    print(item,score.get(item),score[item])

'''key不可重复，重复会覆盖'''
d={'name':'jack','name':'mali'}
print(d)

'''生成式'''
items=['fruit','book','other','jjj']#若item有m个元素，prices有n个，则挑少的生成，即若m<n,m个；m>=n,n个。★
prices=[96,78,85]
d={item:price for item,price in zip(items,prices)}
print(d)