# list 使用
classmates = ['a', 'b', 'c']
print(classmates)
classmateslen = len(classmates)
print(classmateslen)
# 打印出  下标相对应的数据
print(classmates[0])
# 注意： 当索引超出范围 Python 会报 一个IndexError  错误，所以要确保索引不要越界，记得最后一个元素的索引是 len(name)-1
# 栗子：
print(classmates[-1])
#  往list中追加元素到末尾
classmates.append('e')
print(classmates)
#  往list 插入数据到指定位置
classmates.insert(0, 'cha')
print(classmates)
# 删除list 末尾元素 pop()方法
classmates.pop()
print(classmates)
# 删除指定元素 用pop(i) ,i 是 索引位置
classmates.pop(1)
print(classmates)
# 替换某个元素，可以直接赋值给对应的索引位置
classmates[1] = 'chencha'
print(classmates)

