# print 输出
a = 100 + 200 * 2
print('hello world', 'one fist ', a)
# 计算加法
print('100 + 200 = ', 100 + 200)

# 输入 inpit()
name = input()

# -*-
n = 1024 * 768
b = 10 + 20
print(n + b)

# 以冒号： 结尾时，缩进的语句为代码代码块
a = 100
if a >= 0:
    print(a)
else:
    print(-a)

# 字符串
print('I\'m\"Ok"!')

# \ 转移字符
print('\\\t\\')
# r'' 表示''内部的字符串默认不转义
print(r'\\\t\\')
# 如果字符串内部有很多换行，用\n写在一行不好阅读，为了简化，可以会用 '''...'''的格式表示多行内容
print('''line1
... line2
... line3''')

# 布尔型
t1 = True
t2 = False
t3 = 100
if t3 > 101:
    print(t1)
else:
    print(t2)
# 布尔型 and 运算
a1 = True and True
print(a1)
# 布尔型 or 或运算
a2 = True or True
print(a2)
a3 = True or False
print(a3)
a4 = 5 > 3 or 1 > 3
print(a4)

# not 运算
n = not True
print("n->", n)
n1 = not 1 > 2
print("n _ 1 > 2", n1)

# 除法  /   --->  //
c = 10 / 3
print("除法--->", c)
c1 = 10 // 3
print("取整除法----->", c1)
