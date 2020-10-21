# 作者：季毛毛
# 日期：2020/10/6 22:48
# 作用：数据类型转换

name = 'zhangsan'
age = 20
print('我叫' + name + '，今年' + str(age) + '岁')#str()强制类型转换

s1 = '128'
f1 = 98.7
s2 = '128.1'
ff = True
s3 = 'hello'
print(int(s1), type(int(s1)))#转换成功，str转int前提str为数字
print(int(f1), type(int(f1)))#转换成功，但是会省略小数部分
#print(int(s2), type(int(s2)))#转换失败，str转int前提str必须为数字，且为整数
print(int(ff), type(int(ff)))#转换成功
#print(int(s3), type(int(s3)))#转换失败，str必须为数字

#其他转float，若成功则会加数字+.0
i = 1
str = '12'
print(float(i))
print(float(str))