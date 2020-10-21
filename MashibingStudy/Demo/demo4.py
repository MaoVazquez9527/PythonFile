# 作者：季毛毛
# 日期：2020/10/6 22:33
# 作用：数据类型

#整数型
n1 = 250
print(n1, type(n1))
print('二进制', 0b101010111)#零b，0b，不是ob
print('八进制', 0o254641)
print('十六进制', 0x1231ad)

#浮点型
n2 = 3.14159
print(n2, type(n2))

#布尔型,true代表1,false代表0
b1 = True
b2 = False
print(b1, type(b1))
print(b2, type(b2))
print(b1+1, b2+1)#布尔型可以直接转整形进行加减

#字符串类型
str1 = '人生苦短，我用pytho'
str2 = "人生苦短，我用pytho"
str3 = """人生苦短，
我用pytho"""
str4 = '''人生苦短，我用python'''
print(str1, type(str1))
print(str2, type(str2))
print(str3, type(str3))
print(str4, type(str4))

