# 作者：季毛毛
# 日期：2020/10/14 19:28
# 作用：元组

'''可变序列和不可变序列'''
'''可变序列，可进行增删改，例：列表，字典'''
'''不可变序列：字符串，元组'''

'''创建方式'''
'''使用()'''
t=('python','world',98)
print(t)
'''使用tuple()'''
t=tuple(('phthol','world',99))
print(t)
'''可以省略括号'''
t2='python','world',98
print(t2,type(t2))
'''只有一个值时,使用逗号表明是元组'''
t3=('python',)
print(t3,type(t3))
'''空元组的创建'''
lst=[]
lst1=list()#内置函数
print('空列表',lst,lst1)
d={}
d2=dict()
print('空字典',d,d2)
t4=()
t5=tuple()
print('空元组',t4,t5)

'''元组不可变序列的操作'''
t=(10,[20,30],9)
print(t,type(t))
print(t[0],type(t[0]))#int，不可修改
print(t[1],type(t[1]))#list，可修改
print(t[2],type(t[2]))#int，不可修改
'''尝试将t[1]指向100不成功，只能修改t[1]指向的list的内容'''
#t[1]=100#失败
t[1].append(100)
print('修改后t[1]：',t[1],type(t[1]))

'''元组的遍历'''
t=('python','world',98)
for item in t:
    print(item)

