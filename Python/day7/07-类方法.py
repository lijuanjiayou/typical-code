# 自定义一个类
class Person(object):

    # 类属性(私有)
    __country = "中国"

    # 定义类方法
    # 获取私有类属性的值
    # cls = 类名
    # 修饰器
    @classmethod
    def get_country(cls):
        return cls.__country

    # 修改私有类属性的值
    @classmethod
    def set_country(cls, new_country):
        cls.__country = new_country

# 01: 类名.类方法(调用类方法)
# print(Person.get_country())
#
# Person.set_country("中华")
#
# print(Person.get_country())

# 02: 对象名.类方法(调用类方法)
xiaoming = Person()
# 调用类方法
print(xiaoming.get_country())
xiaoming.set_country("中华")
print(xiaoming.get_country())







