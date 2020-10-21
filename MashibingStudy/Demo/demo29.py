# 作者：季毛毛
# 日期：2020/10/20 10:26
# 作用：封装，继承，方法重写，多态

'''封装'''
class Car:
    def __init__(self,brand):
        self.brand=brand

    def start(self):
        print('汽车已启动')

car=Car('宝马x5')
car.start()
print(car.brand)

class Student:
    def __init__(self,name,age):
        self.name=name
        self.__age=age#这样age不能在类的外部使用

    def show(self):
        print(self.name,self.__age)

stu=Student('张三',20)
stu.show()
#print(stu.age)报错，age不可在类外部使用
print(dir(stu))
print(stu._Student__age)#在类的外部可以通过这样使用

'''继承'''
print('------继承-------')
class Person(object):
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def info(self):
        print(self.name,self.age)

class Student(Person):
    def __init__(self,name,age,stu_no):
        super().__init__(name,age)
        self.stu_no=stu_no

class Teacher(Person):
    def __init__(self,name,age,teachofyear):
        super().__init__(name,age)
        self.teachofyear=teachofyear

stu=Student('张三',20,'1001')
teacher=Teacher('李四',34,10)
stu.info()
teacher.info()

'''多继承'''
print('---------多继承--------')
class A(object):
    pass
class B(object):
    pass
class C(A,B):
    pass

print('----------方法重写------------')
class Person(object):
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def info(self):
        print(self.name,self.age)

class Student(Person):
    def __init__(self,name,age,stu_no):
        super().__init__(name,age)
        self.stu_no=stu_no
    def info(self):
        super().info()
        print(self.stu_no)

class Teacher(Person):
    def __init__(self,name,age,teachofyear):
        super().__init__(name,age)
        self.teachofyear=teachofyear
    def info(self):
        super().info()
        print(self.teachofyear)

stu=Student('张三',20,'1001')
teacher=Teacher('李四',34,10)
stu.info()
teacher.info()

print('------------多态-------------')
class Animal(object):
    def eat(self):
        print('动物会吃')

class Dog(Animal):
    def eat(self):
        print('狗吃骨头')

class Cat(Animal):
    def eat(self):
        print('猫吃鱼')

class Person(object):
    def eat(self):
        print('人吃饭')

def fun(obj):
    obj.eat()

fun(Cat())
fun(Dog())
fun(Person())