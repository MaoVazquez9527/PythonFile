# 作者：季毛毛
# 日期：2020/10/21 16:07
# 作用：os模块

import os
#os.system('notepad.exe')
#os.system('calc.exe')
'''直接调用可执行文件'''
#os.startfile('D:\\QQ\\Bin\\QQScLauncher.exe')

'''常用函数'''
print(os.getcwd())
lst=os.listdir('..')
print(lst)