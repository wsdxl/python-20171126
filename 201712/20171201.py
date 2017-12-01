"""
通用序列操作
"""
#1.1 索引
a='asdffhkyfhjjzxcv'
print(a[1])
print(a[4])
print(a[-1])
print(a[-2])
print("===============")
# 1.2 分片
print(a[1:4])
print(a[8::-2])
b='0123456789'
print(b[5::-2])
print(b[5::2])
#1.3 序列相加
x=[1,3,5]
y=[2,4,6]
a='hello'
b='world'
c='1'
print(x+y)
print(a+b)
print(a,b)
print(a+c)
# 1.4 相乘
a=[1,3,5]
b=[2,4,6]
c=5
x='hello'
print(a*c)   #a被复制了5遍
print(x*c)

# 1.5 成员资格
a=[1,2,3,4,5,6,7,8,9]
b='helloworld'
print(1 in a)
print(10 in a)
print('he' in b)
print('old' in b)