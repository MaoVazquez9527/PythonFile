# 作者：季毛毛
# 日期：2020/10/12 9:46
# 作用：循环结构，break使用

#while 循环
a=1
while a<10:#判断次数比执行次数多1
    print(a)
    a+=1

#计算1~100之间的偶数和
sum=0
a=2
while a<=100:
    sum+=a
    a+=2
print('结果为：',sum)

#for-in循环,可迭代对象：字符串和序列
for item in 'python':
    print(item)

for item in range(10):
    print(item)

for _ in range(5):#不适用自定义变量则循环五次
    print('you are sb')

#计算1-100间偶数和
sum=0
for item in range(1,101):
    if item%2==0:
        sum+=item
print('结果为；',sum)

#输出100-999之间的水仙花数
for item in range(100,1000):
    ge=item%10#求个位数
    shi=item//10%10#求十位数
    bai=item//100#求百位数
    if ge**3+shi**3+bai**3==item:
        print('水仙花数：',item)

#break使用，模拟密码输入
for item in range(3):
    pwd=input('请输入密码：')
    if pwd=='8888':
        print('true')
        break
    else:print('flase')

a=0
while a<3:
    pwd=input('请输入密码：')
    if pwd=='8888':
        print('true')
        break
    else:
        print('flase')
    a+=1