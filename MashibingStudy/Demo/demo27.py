# 作者：季毛毛
# 日期：2020/10/19 18:58
# 作用：异常捕获

'''try.....except...else....finally'''
try:#可能会出错的代码
    n1=int(input('输入第一个数：'))
    n2=int(input('输入第二个数：'))
    res=n1/n2
except BaseException as e:#出错执行的代码
    print('错误为：',e)
else:#正常执行的代码
    print('结果为：',res)
finally:
    print('不管出不出错都执行的代码')
