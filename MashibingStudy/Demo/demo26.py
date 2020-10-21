# 作者：季毛毛
# 日期：2020/10/19 13:22
# 作用：递归函数

def fac(n):
    if n==1:
        return 1
    else:
        return n*fac(n-1)
print(fac(5))

'''斐波那契数列'''
def fib(n):
    if n==1:
        return 1
    elif n==2:
        return 1
    return fib(n-1)+fib(n-2)
num=input('输入数字：')
print('第',num,'位数字为：',fib(int(num)))
print('前',num,'位数字为：')
for i in range(1,int(num)+1):
    print(fib(i))