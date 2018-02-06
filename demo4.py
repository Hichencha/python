# 1. for ... in 循环，依次吧list 或 tuple 中的每个元素迭代
names = ['a', 'b', 'c', 'd']
for name in names:
    print('for ... in', name)

# 2. for x in...  循环就是把每个元素带入变量x ，然后执行缩进块的语句
sum = 0
for x in [1, 2, 3, 4, 5, 6, 7, 8, 9]:
    sum = sum + x
print('for x in', sum)
# 3. range() 函数，可以生成一个整数序列，再通过list() 函数可以转换为list
suma = 0
for x in range(101):
    suma = suma + x
print(' range', suma)
# 4. while 循环  在循环内部变量n不断自减，直到变为-1时，不再满足while条件，循环退出。
sum = 0
n = 99
while n > 0:
    sum = sum + n
    n = n - 2
print('while',sum)


