
# 自定义一个人类
class Person(object):

    def __init__(self):

        self.name = "小明"
        self.__age = 20

    # 定义一个方法(获取属性的值 一般方法名中使用get)
    def get_age(self):
        return self.__age

    # 定义一个方法(对属性赋值的时候 一般方法名中使用set)
    def set_age(self, new_age):
        self.__age = new_age



# 间接的修改私有属性的值 和获取私有属性的值
# 对象
xiaoming = Person()
# print(xiaoming.name)

# 01 使用对象调用私有属性 完成打印age的值
print(xiaoming.get_age())
# 02 使用对象设置私有属性的值
xiaoming.set_age(30)

# 测试
print(xiaoming.get_age())