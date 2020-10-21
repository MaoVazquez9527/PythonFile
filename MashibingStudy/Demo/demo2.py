# 作者：季毛毛
# 日期：2020/10/4 22:11
# 作用：转义字符

print('hello\nworld')
print('hello\tworld')#一个'\t'占一个制表位，即四个空格，所以'hell' 'o   ' 'worl' 'd'
print('helloooo\tworld')#'hell' 'oooo' '    ' 'worl' 'd'总之\t补全不够的位置
print('hello\rworld')#\r之后的顶替之前的
print('hello\bworld')#\b覆盖一格，顶掉'o'

print('老师说:\'大家好\'')#输出单引号
print('\\')#输出反斜杠

#原字符，不希望字符串中的转义字符起作用，使用原字符就是在字符串之前加上r，或R
print(r'hello\nworld')

