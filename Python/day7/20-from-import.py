# 格式: from 模块名 import 全局变量  函数  类
from hm_sum import name, add2num, Person

# 使用from-import 在使用的时候 不需要在写模块名
# 注意和本模块的名字冲突
print(name)

# def add2num(a, b):
#     return a - b

print(add2num(10, 20))
p = Person()
p.eat()