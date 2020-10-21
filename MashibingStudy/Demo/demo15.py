# 作者：季毛毛
# 日期：2020/10/12 10:42
# 作用：continue

#使用continue输出1-50之间5的倍数
for item in range(1,51):
    if item%5!=0:
        continue
    print(item)
