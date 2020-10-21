# 作者：季毛毛
# 日期：2020/10/12 9:36
# 作用：range函数的使用

#range的三种创建方式
r=range(10)
print(r)
print(list(r))

r=range(1,10)#从1开始，10结束，不包括10
print(list(r))

r=range(1,10,2)#起始，结束，步长
print(list(r))
#判断数字是否在序列中,in   not in
print(10 in r)
print(9 in list(r))