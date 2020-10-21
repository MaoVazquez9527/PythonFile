# 作者：季毛毛
# 日期：2020/10/19 19:18
# 作用：类

class Student:
    native_place='makabaka'#类属性

    def __init__(self,name,age):
        self.name=name
        self.age=age

    def eat(self):#实例方法
        print(self.name,'在奥里给')

    @staticmethod
    def method():#静态方法
        print('静态方法')

    @classmethod
    def cm(cls):#类方法
        print('类方法')

'''创建类对象'''
stu1=Student('zhangsan',20)
print(stu1.name)
'''功能相同，写法不一样'''
stu1.eat()
Student.eat(stu1)
print(stu1.native_place)

'''动态绑定属性'''
stu1=Student('张三',20)
stu2=Student('李四',25)
stu1.gender='女'
print(stu1.name,stu1.age,stu1.gender)
#print(stu2.name,stu2.age,stu2.gender)
'''动态绑定方法'''
stu1.eat()
stu2.eat()
def show():
    print('定义在类之外')
stu1.show=show()#绑定show方法
stu1.show
#stu2.show报错，没有绑定