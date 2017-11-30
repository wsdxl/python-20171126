"""
===
author:wsdxl
===
date:2017-11-28
"""

# # 算数运算符
# a = 21
# b = 10
# c = 0
# c = a + b
# print('Line1 - value of c is', c)
# c = a - b
# print('Line2 - value of c is', c)
# c = a * b
# print('Line3 - value of c is', c)
# c = a / b
# print('Line4 - value of c is', c)
# c = a % b
# print('Line5 - value of c is', c)

# a = 2
# b = 3
# c = a**b
# print('Line6 - value of c is', c)

# a = 10
# b = 5
# c = a // b
# print('Line7 - value of c is', c)

# # python比较运算符
# a = 21
# b = 10
# c = 0
# if (a == b):
#     print('Line1 - a is equal to b')
# else:
#     print('line1 - a is not equal to b')

# if (a != b):
#     print('line2 - a is not equal to b')
# else:
#     print('Line2 - a is equal to b')
# # if (a <> b):                                 #Python3.6版本不支持
# #     print('line3 - a is not equal to b')
# # else:
# #     print('Line3 - a is equal to b')
# if (a<b):
#     print('line4 - a is less than b')
# else:
#     print('Line4 - a is not less than b')
# if (a>b):
#     print('line5 - a is greater than b')
# else:
#     print('Line5 - a is not greater than b')
# if (a<=b):
#     print('line6 - a is either less than or equal to b')
# else:
#     print('Line6 - a is neither less than nor eaual to b')
# if (a>=b):
#     print('line7 - a is either greater than or equal to b')
# else:
#     print('Line7 - a is neither greater than nor equal to b')

# # python赋值运算符
# a=21
# b=10
# c=0

# c=a+b
# print('Line1 - value of c is',c)

# c+=a
# print('Line2 - value of c is',c)

# c*=a
# print('Line3 - value of c is',c)

# c/=a
# print('Line4 - value of c is',c)

# c=2
# c%=a
# print('Line5 - value of c is',c)

# c**=a
# print('Line6 - value of c is',c)

# c//=a
# print('Line7 - value of c is',c)

# python位运算符
a=60   #60=00111100
b=13   #13=00001101
c=0
c=a & b
# print('Line1 - value of c is',c)
# c=a | b
# print('Line2 - value of c is',c)
# c= a ^ b
# print('Line3 - value of c is',c)    
c= ~ a
print('Line4 - vaule of c is',c) #为什么是-61? ->11000011 减1得1000010然后取反得到0111101转换为十进制是61,首位1代表符号负号，所以结果为-61
# c= a << 2
# print('Line5 - vaule of c is',c)
# c= a >> 2
# print('Line6 - vaule of c is',c)

# # python逻辑运算符
# a = 10
# b = 20
# c = 0
# if (a and b):
#     print('Line1 - a and  b are true')
# else:
#     print('Line1 - either a is not true or b is not true')
# if (a or b):
#     print('line2 - either a is true or b is true or both are true')
# else:
#     print('line2 - neither a is  true nor b is  true')

# a=0
# if(a and b):
#     print('Line3 - a and  b are true')
# else:
#     print('Line3 - either a is not true or b is not true')

# if(a or b):
#     print('line4 - either a is true or b is true or both are true')
# else:
#     print('line4 - neither a is  true nor b is  true')

# if not(a and b):
#     print('Line5 - a and  b are true')
# else:
#     print('Line5 - either a is not true or b is not true')

# # python 成员运算符
# a=10
# b=20
# list=[1,2,3,4,5]
# if(a in list):
#     print('Line 1 - a is available in the given list')
# else:
#     print('Line 1 -a is not available in the given list')
# if(b not in list):
#     print('Line 2 - b is not available in the given list')
# else:
#     print('Line 2 - b is available the given list')

# a=2
# if(a in list):
#     print('Line 3 - a is available in the given list')
# else:
#     print ('Line 3 - a is not available in the given list')

# # Python 身份运算符
# a=20
# b=20

# if(a is b):
#     print('Line 1 - a and b have same identity')
# else:
#     print('Line 1 - a and b do not have same identity')

# if(id(a) == id(b)):
#     print('Line 2 - a and b have same identity')
# else:
#     print('Line 2 - a and b do not have same identity')


# b=30
# if(a is b):
#     print('Line 3 - a and b have same identity')
# else:
#     print('Line 3 - a and b do not have same identity')

# if(a is not b):
#     print('Line 4 - a and b do not have same identity')
# else:
#     print('Line 4 - a and b have same identity')

# # Python 运算符优先级

# a=20
# b=10
# c=15
# d=5
# e=0

# e=(a+b)*c/d
# print('value of (a+b)*c/d is',e)

# e=((a+b)*c) / d
# print('value of e=((a+b)*c) / d is ',e)

# e=(a+b)*(c/d)
# print ('value of e=(a+b)*(c/d) is ',e)

# e=a+(b*c)/d
# print('value of e=a+(b*c)/d is ',e)
