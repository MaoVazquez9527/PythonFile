# 作者：季毛毛
# 日期：2020/10/20 10:57
# 作用：object 类

class Student:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def __str__(self):
        return '我的名字是{0},今年{1}岁'.format(self.name,self.age)

stu=Student('张三',20)
print(dir(stu))
'''默认调用str函数，没有重写则输出对象的内存地址★ - '''
print(stu)