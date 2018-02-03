# python 字符串是以Unicode 编码，Python的字符串支持多语言
print('包含中午的str')
# 对于单个字符的编码，Python提供了ord() 函数获取字符的整数表示， chr() 函数把编码转换为对应的字符
print("ord----->", ord('A'))
print("chr----->", chr(66))

#  bytes 类型的数据用带 b 前缀的单引号或者双引号
x = b'ABC'
print(x)

# 以Unicode 表示str 通过encode() 方法可以编码为指定的bytes
x1 = 'ABC'.encode('ascii')
print("encode----->", x1)
#  在bytes中，无法显示为ASCII字符的字节，用 \x##显示
x2 = b'\xe4\xb8\xad\xe6\x96\x87'.decode('utf-8')
print(x2)
# 如果bytes 中只有一小部分无效的字节，可以传入 errors = 'ignore'忽略错误的字节
x3 = b'\xe4\xb8\xad\xff'.decode('utf-8', errors='ignore')
print("err错误---->", x3)
# len() 计算str包含多少个字符
slen = len('ABC')
print(slen)
# len() 计算str字符，如果换成bytes
slen1 = len('\xe4\xb8\xad\xe6\x96\x87')
print(slen1)
slen2 = len('中文'.encode('utf-8'))
print(slen2)


