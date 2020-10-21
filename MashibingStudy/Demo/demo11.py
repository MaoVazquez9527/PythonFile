# 作者：季毛毛
# 日期：2020/10/10 16:50
# 作用：分支结构

#单分支结构
money=1000
s=int(input("请输入金额："))
if money>=s:
    money-=s
    print('成功,余额为：',money)

#双分支结构
num=int(input("please input a number:"))
if num%2==0:
    print(num,'是偶数')
else:
    print(num,'是奇数')

#多分支结构
score=int(input("请输入一个成绩"))
if score>=90 and score<=100:
    print('A')
elif score>=80 and score<=89:
    print('B')
elif score>=70 and score<=79:
    print('C')
elif score>=60 and score<=69:
    print('D')
elif score>=0 and score<=59:
    print('E')
else:
    print('请输入有效的成绩')

#嵌套if
answer=input('is vip?y/n')
money=float(input('input money：'))
if answer=='y':
    print('vip')
    if money>=200:
        print('pay:',money*0.8)
    elif money>=100:
        print('pay:',money*0.9)
    else:
        print('pay:',money)

else:
    print('not vip')
    if money>=200:
        print('pay:',money*0.9)
    else:
        print('pay',money)