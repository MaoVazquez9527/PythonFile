# 作者：季毛毛
# 日期：2020/10/13 14:23
# 作用：列表

#两种创建方式
lst2=list(['hello','world'])
lst=['hello','world',927]
print(id(lst))
print(type(lst))
print(lst)
print(lst[0],lst[-3])#正向从0开始计数，逆向从-1开始计数★

#index函数
lst=['hello','world',9527,'hello']
print(lst.index('hello'))#相同元素只返回第一个元素的索引
print(lst.index('hello',1,4))#从索引1-4中寻找hello，不包括4

#切片，切出来的是一个新的列表，有新的id，参数：start,stop,step
lst=[10,20,30,40,50,60,70,80,90]
lst2=lst[1:6:1]#默认步长为1
print(lst2)
#step为正数
print(lst[1:6:])#step默认1
print(lst[:6:2])#start默认1
print(lst[1::2])#stop默认到结束
#step为负数
print(lst[::-1])#倒序
print(lst[7::-1])
print(lst[6:0:-2])


