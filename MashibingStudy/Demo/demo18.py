# 作者：季毛毛
# 日期：2020/10/13 15:14
# 作用：列表函数

lst=[10,20,30]

#添加
lst.append(40)#末尾添加一个
print(lst)
lst2=['hello','world']
lst.append(lst2)#将列表作为一个元素添加到列表
print(lst)
lst.extend(lst2)#将列表的元素依次添加到列表中
print(lst)
lst.insert(0,00)#指定位置添加一个元素
print(lst)
lst3=['hhh','ggg']#指定位置替换元素
lst[1:]=lst3
print(lst)

#删除
lst=[10,20,30,40,50,60,30]
lst.remove(30)#重复元素，则移除第一个
print(lst)
lst.pop(1)
print(lst)
lst.pop()#不指定索引，默认删除最后一个元素
print(lst)
lst2=lst[1:3]#切片，原列表不做改变
print('lst2',lst2)
print(lst)
lst[1:3]=[]#用空列表代替1-3位置的元素，相当于删除★
print(lst)
lst.clear() #清空所有元素
print(lst)

#修改
lst=[10,20,30,40]
lst[0]=100#一次修改一个值
print(lst)
lst[1:2]=[200]
print(lst)

#排序
lst=[10,50,40,30,60,20,80]
print(lst)
lst.sort()#默认升序
print(lst)
lst.sort(reverse=True)#降序排序
print(lst)
lst=[10,50,40,30,60,20,80]
print(lst,id(lst))
lst2=sorted(lst)#新的id，新的列表
print(lst2,id(lst2))
lst3=sorted(lst,reverse=True)
print(lst3,id(lst3))

#列表生成
lst=[i for i in range(1,10)]
print(lst)
lst=[i*i for i in range(1,10)]
print(lst)
#列表中的元素值为2，4，6，8，10
lst2=[i*2for i in range(1,6)]
print(lst2)