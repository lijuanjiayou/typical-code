
# 了解(需要调试程序)

# 自定义一个人类
class Person(object):

    def __init__(self, name):
        self.name = name


    def eat(self):
        print("人会吃饭")
        print("="*10)



# 内存地址问题

xiaoming = Person("小明")
# print(id(xiaoming))
# print(id(xiaoming.name))
print(id(xiaoming.eat()))


xiaohong = Person("小红")
# print(id(xiaohong))
# print(id(xiaohong.name))
print(id(xiaohong.eat()))


"""
对象需要占用地址(和对象属性地址不同) 表达的是不同的人
对象的属性也要占用地址(和对象的地址不同) 不同的人属性特征是不同的
# 不同的对象 但是调用的对象方法的id(地址相同)相同(方法相同 因为方法中有一个形参self 可以区分是哪个对象调用的)

"""