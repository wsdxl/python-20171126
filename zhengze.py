'''
正则表达式
'''
import re
# a=re.match(r'^\d{3}\-\d{3,8}$','010-12345')
# print(a)
# b=re.split(r'\s+','a b   c')
# print(b)

# c=re.split(r'[\s\,]','a,b c d')
# print(c)
# d=re.split(r'[\s\,\;]','a,b;c d')
# print(d)

# #分组
# m=re.match(r'^(\d{3})-(\d{3,8})$','010-1234567')
# print(m.group())
# print(m.group(1))
# print(m.group(2))

# #更加凶残的例子
# t = '19:05:30'
# m = re.match(
#     r'^(0[0-9]|1[0-9]|2[0-3]|[0-9])\:(0[0-9]|1[0-9]|2[0-9]|3[0-9]|4[0-9]|5[0-9]|[0-9])\:(0[0-9]|1[0-9]|2[0-9]|3[0-9]|4[0-9]|5[0-9]|[0-9])$',
#     t)
# print(m.groups())
# print(m.group(1))

# #贪婪匹配
# e=re.match(r'^(\d+?)(0*)$', '102300').groups()
# print(e)

# #编译

# # 编译:
# re_telephone = re.compile(r'^(\d{3})-(\d{3,8})$')
# # 使用：
# x=re_telephone.match('010-12345')
# print(x.groups())
# y=re_telephone.match('021-8081')
# print(y.groups())

'''
编写正则表达式验证一下邮箱
someone@gmail.com
bill.gates@microsoft.com
'''
re_email=re.compile(r'^([0-9a-zA-Z\.\_]{2,10})@([0-9a-zA-Z\_]+).([0-9a-zA-Z\_]+)$')
o=re_email.match('dxl20@163.com')
m=re_email.match('bill.gates@microsoft.com')
print(o.group())
print(o.group(1))
print(o.group(2))
print(o.group(3))
print(m.group())
print(m.group(1))
print(m.group(2))
print(m.group(3))