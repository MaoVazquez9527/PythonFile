# 作者：季毛毛
# 日期：2020/10/11 9:45
# 作用：条件表达式

num_a=int(input('请输入第一个整数：'))
num_b=int(input('请输入第二个整数：'))
#正常比较大小
if num_a>=num_b:
    print(num_a,'大于等于',num_b)
else:
    print(num_a,'小于',num_b)
#使用条件表达式进行比较
print(str(num_a)+'大于等于'+str(num_b) if num_a>=num_b else str(num_a)+'小于'+str(num_b))
