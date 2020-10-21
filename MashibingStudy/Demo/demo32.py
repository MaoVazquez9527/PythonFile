# 作者：季毛毛
# 日期：2020/10/21 8:37
# 作用：文件读写

print('----------读----------')
file=open('demo1.txt', 'r', encoding='utf-8')#r代表读操作
'''三个不能同时使用'''
print('readlines',file.readlines())
#print('read',file.read(2))
#print('readline',file.readline(2))
file.close()

print('-----------写----------')
file=open('a.txt', 'w', encoding='utf-8')#w代表写
file.write('helloworld')
file.close()

print('-----------追加写-------------')
file=open('a.txt', 'a', encoding='utf-8')#w代表写
file.write('python')
file.write('python')
file.write('python')
file.close()

print('------不用写close语句---------')
with open('a.txt', 'r') as file:
    print(file.read())