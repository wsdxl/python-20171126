"""
字符串的操作

"""
name = 'xiaoming'
address = "china"
age=18
money=50.25
print(name, address)
print(name+address)
print(name+' '+address)
print('my name is %s'%name)  #%s是string占位符
print('my name is %s,i live in %s,i am %d years old,i have %g money'%(name,address,age,money)) #%d是数字类型的占位符,小数输出要使用%f,%g也可以表示小数，并且会自动不显示无意义的0

print(name*2)     #复制