# 作者：季毛毛
# 日期：2020/10/15 15:59
# 作用：

import copy

'''copy()和deepcopy()'''
a=['a',[1,2,3,4]]
b=a
'''a，c是独立的对象，但指向同一对象，改变a，c也会同时改变'''
c=a.copy()
'''a，d是独立的对象，指向不同的对象'''
d=copy.deepcopy(a)
print('a',a,id(a))
print('b',b,id(b))
print('c',c,id(c))
print('d',d,id(d))
'''修改a[n]的元素，浅copy和deepcopy的值不会改变'''
a.append('a')
print(a)
print(b)
print(c)
print(d)
'''改变a中list的元素时，浅copy改变，deepcopy不改变'''
a[1][0]='python'
print(a)
print(b)
print(c)
print(d)

''''''
