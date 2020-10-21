# 作者：季毛毛
# 日期：2020/10/17 9:12
# 作用：函数

def fun(arg1,arg2):
    print('arg1',arg1)
    print('arg2',arg2)
    arg1=100
    arg2.append(10)
    print('arg1',arg1)
    print('arg2',arg2)

n1=11
n2=[22,33,44]
print(n1)
print(n2)
print('-------------')
fun(n1,n2)
print(n1)
print(n2)

def fun(num):
    odd=[]#存奇数
    even=[]#存偶数
    for i in num:
        if i%2:
            odd.append(i)
        else:
            even.append(i)
    return odd,even

print((fun([10,29,34,23,44,53,55])))

def fun1():
    print('f1 hello')
fun1()

def fun2():
    return 'f2 hello'
res=fun2()
print(res)

def fun3():
    return 'hello','world'
print(fun3())

def fun(a,b=10):
    print(a,b)
'''没有参数将使用默认参数'''
fun(100)
'''都定义就使用参数'''
fun(20,30)

'''不确定参数个数,结果为元组'''
def fun(*args):
    print(args)
fun(10)
fun(10,20,30)
'''不确定参数个数,结果为字典'''
def fun(**args):
    print(args)
fun(a=10)
fun(a=10,b=20)

'''函数总结'''
def fun(a,b,c):
    print('a=',a)
    print('b=',b)
    print('c=',c)
fun(10,20,30)
lst=[10,20,30]
fun(*lst)
dict={'a':10,'b':20,'c':30}
fun(**dict)