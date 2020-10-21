# 作者：季毛毛
# 日期：2020/10/4 21:48
# 作用：print()函数测试

#可以输出数字
print(520)
print(98.5)

#可以输出字符串
print('hello world')

#可以输出含有运算符的表达式
print(3+1)

#将数据输出到文件中   注:盘存在；使用中间变量fp
fp=open('E:/PyCharm/Python/venv/demo1.txt','a+')
print('hello world', file=fp)
fp.close()