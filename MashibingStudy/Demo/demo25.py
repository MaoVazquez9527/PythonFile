# 作者：季毛毛
# 日期：2020/10/19 13:11
# 作用：变量的作用域

def fun(a,b):
    c=a+b#c就称为局部变量，定义在函数内部
    print(c)

name='***'#name为全局变量
def fun2():
    print(name)
fun2()

'''使用global申明的局部变量相当于全局变量'''
def fun3():
    global age
    age=20
fun3()
print(age)