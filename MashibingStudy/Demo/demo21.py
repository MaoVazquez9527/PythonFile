# 作者：季毛毛
# 日期：2020/10/14 19:53
# 作用：集合

'''创建方式'''
'''相当于没有value的字典，key的值唯一'''
s={2,3,4,5,5,6,7,8,8,8}
print(s)
'''set()创建'''
s=set(range(6))
print(s,type(s))
s=set([1,2,3,4,5])#将list内容转为集合的值
print(s,type(s))
s=set((1,2,3,4,4,6,7,65))#将元组内容转为集合的值,注意顺序
print(s,type(s))
s=set('python')#字符串转集合
print(s,type(s))
s=set({12,4,34,55,66,44,4})#集合转集合，去掉重复元素
print(s,type(s))
'''定义空集合'''
s=set()
print(s,type(s))

'''判断'''
s={10,20,30,40,50,60}
print(10 in s)
print(100 in s)

'''添加'''
s.add(70)#添加一个
print(s)
s.update({80,90})#添加多个，例如集合
print(s)
s.update((100,200))#添加多个，例如元组
print(s)
s.update([300,400])#添加多个，例如数组
print(s)

'''删除'''
'''remove，删除一个，不存在报错'''
s.remove(400)
print(s)
#s.remove(500)#error
'''discard,删除一个，不存在不报错'''
s.discard(500)
'''pop,删除一个，随机删除'''
s.pop()
print(s)
'''clear,清空'''
s.clear()

'''集合间的关系'''
'''相等'''
s={10,20,30,40}
s2={20,30,10,40}
print(s==s2)
'''子集关系'''
s={10,20,30,40}
s2={10,30}
s3={10,50,30}
print('s2是s的子集',s2.issubset(s))
print(s3.issubset(s))
print('s是s2的父集',s.issuperset(s2))
print(s.issuperset(s3))
'''交集'''
s={10,20,30,40}
s2={10,50,30}
s3={100,200,300}
print(s.isdisjoint(s2))#false 表示有交集
print(s.isdisjoint(s3))#true 表示没有交集

'''集合的数学操作'''
'''交集'''
s1={10,20,30,40}
s2={20,30,40,50,60}
print(s1.intersection(s2))
print(s1 & s2)
'''并集'''
s1={10,20,30,40}
s2={20,30,40,50,60}
print(s1.union(s2))
print(s1 | s2)
print(s1)#不改变原集合
'''差集'''
s1={10,20,30,40}
s2={20,30,40,50,60}
print(s1.difference(s2))
print(s1-s2)
'''对称差集'''
print(s1.symmetric_difference(s2))
print(s1^s2)#键盘6键

'''集合生成式'''
lst=[i*i for i in range(6)]#列表生成式
print(lst)
'''将[]换成{}'''
s={i*i for i in range(6)}
print(s)