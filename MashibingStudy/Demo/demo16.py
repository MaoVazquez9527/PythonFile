# 作者：季毛毛
# 日期：2020/10/13 13:54
# 作用：嵌套循环

#三行四列的矩形
for i in range(1,4):
    for j in range(1,5):
        print('*',end='\t')#end不换行输出
    print()

#乘法表格式
for i in range(1,10):
    j = 1
    while j<=i:
        print('*',end='\t')
        j+=1
    print()
#老师方法
for i in range(1,10):
    for j in range(1,i+1):
        print(i,'*',j,'=',i*j,end='\t')
    print()
