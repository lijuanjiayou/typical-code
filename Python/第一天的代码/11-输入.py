# 主要学习python3.x的输入

# python3.x程序的输入使用的input
# input 得到的结果是字符串类型
my_name = input("请输入您的名字:")
# 输入年龄
my_age = input("请输入您的年龄:")
# <class 'str'>
print(type(my_age))
# 小明 22
# 如果想通过打印完成多个变量的输出 print(变量名1, 变量名2, ....)
# print(my_name, my_age)
# 名字:小明 年龄:22岁
print("名字:%s 年龄:%s岁" %(my_name, my_age))


# python2.x 了解
# python2.x中的raw_input 等价于 python3.x中的input 无论输入是什么类型 最终都是字符串
# python2.x中的input 对应的变量类型是看用户的数据类型