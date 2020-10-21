# 作者：季毛毛
# 日期：2020/10/14 22:54
# 作用：字符串

a='python'
b="python"
c='''python'''
print(a,id(a))
print(b,id(b))
print(c,id(c))

'''常用操作'''
s='hello,hello'
'''正向'''
print(s.index('lo'))
print(s.find('lo'))
'''逆向'''
print(s.rindex('lo'))
print(s.rfind('lo'))
'''查找不存在'''
#print(s.index('k'))#报错，不建议使用
print(s.find('k'))

'''大小写转换'''
s='hello,python'
'''转大写'''
a=s.upper()
print(a)
'''转小写'''
b=a.lower()
print(b)
'''大转小，小转大'''
s='Hello,Python'
print(s.swapcase())
'''开头字母大写，其他小写'''
print(s.title())

'''字符串对齐'''
s='hello,Python'
print(s.center(20,'*',))#20为设定的宽度，大于s长度用*补充，不足返回原字符串
print(s.ljust(20,'*'))
print(s.rjust(20,'*'))
print(s.zfill(20))#使用0填充

'''分割操作'''
s='hello world python'
print(s.split())
s='hello,world,python'
print(s.split(sep=','))
print(s.split(sep=',',maxsplit=1))#分一次
'''rsplit'''
print(s.rsplit(sep=','))
print(s.rsplit(sep=',',maxsplit=1))#区别

'''字符串判断'''
s='hello,python'
'''不是合法的字符，合法的字符由：字母、数字和下划线组成。汉字等同字母'''
print(s.isidentifier())
print('hello'.isidentifier())
print('张三'.isidentifier())
'''是否全由字母组成'''
print(s.isalpha())
print('hello'.isalpha())
print('张三'.isalpha())
print('张三1'.isalpha())#1不是字母
'''是否由十进制数字组成'''
print('111'.isdecimal())
print('452四'.isdecimal())
'''是否由数字组成'''
print('111'.isnumeric())
print('452四'.isnumeric())
'''是否由数字和字母组成'''
print('1235das'.isalnum())
print('张三465da'.isalnum())
print('555dssd!'.isalnum())

'''字符串替换'''
s='hello,python'
print(s.replace('python','java'))
s='hello,python,python,python'
'''替换两次，靠前替换'''
print(s.replace('python','java',2))

'''连接'''
lst=['hello','java','python']
print('|'.join(lst))
tup=('hello','java','python')
print('?'.join(tup))
print('*'.join('python'))#★

'''比较'''
print('apple'>'app')
print('apple'>'banana')
print(ord('a'),ord('b'))

'''切片'''
s='hello,python'
'''不写开头则默认从0开始切'''
s1=s[:5]
print(s1)
'''不写结尾默认切到结尾'''
s2=s[6:]
print(s2)
s3='!'
newstr=s1+s3+s2
print(newstr)
'''完整写法'''
print(s[0:5:1])
'''步长为+，不写开头结尾，默认开头切到结尾'''
print(s[::2])
'''步长为-，不写开头结尾，默认结尾切到靠头，倒置'''
print(s[::-1])

'''格式化字符串'''
'''%占位符'''
name='zhangsan'
age=20
print('wojiao%s,jinnian%dsui' % (name,age))
'''{}占位符'''
print('wojiao{0},jinnian{1}sui'.format(name,age))
'''f-string'''
print(f'wojiao{name},jinnian{age}sui')

'''宽度和精度'''
'''宽度'''
print('%10d' % 9)#10表示宽度为10
print('**********')
'''精度'''
print('%.3f' % 3.1415927)#保留三位小数
print('{0:.3f}'.format(3.1415927))#三位小数
print('{0:.3}'.format(3.1415927))#三位有效数字
'''同时表示宽度和精度'''
print('%10.3f' % 3.1415927)

'''编码转换'''
s='天涯共此时'
'''编码'''
print(s.encode(encoding='GBK'))#gbk中一个中文占两个字节
print(s.encode(encoding='UTF-8'))#utf-8中一个中文占三个字节
'''解码'''
byte=s.encode(encoding='GBK')
print(byte.decode(encoding='GBK'))
'''同一种编码对应一种解码'''
#print(byte.decode(encoding='UTF-8'))#error