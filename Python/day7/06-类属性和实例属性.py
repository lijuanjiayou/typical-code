# 自定义一个类
class Person(object):
    # 国家
    country = "中国"

    def __init__(self, name, age):
        # 实例属性(对象属性)
        self.name = name
        self.age = age


# xiaoming = Person("小明", 20)
#
# # 使用实例属性: 对象名.实例属性名
# # print(xiaoming.name)
#
# # 修改实例属性: 对象名.实例属性名 = 值
# xiaoming.name = "小明明"
# print(xiaoming.name)

# 使用类属性
# 01: 类名.类属性名
# print(Person.country)
# 02: 对象名.类属性名
# xiaoming = Person("小明", 20)
# print(xiaoming.country)


# 修改类属性
# 01: 类名.类属性名 = 值
# Person.country = "中华"
# print(Person.country)

# 02: 不存在(对象名.类属性名 = 值)
# xiaoming = Person("小明", 20)
# # python认为你是给对象设置实例属性(只是和类属性名相同而已)
# xiaoming.country = "中华"
# print(xiaoming.country)
# print(Person.country)


# 关于类属性 内存问题
# xiaoming1 = Person("小明1", 20)
# xiaoming2 = Person("小明2", 20)
# 类属性python只会开辟一份内存(他是代表这个类的属性这个类python中只有一个)
# print(id(xiaoming1.country))
# print(id(xiaoming2.country))
# print(id(Person.country))


# 类属性好处???
# 为了节约内存
# 为了后期业务需求更改 可以提高开发效率
# 自定义一个类
class Person(object):
    # 国家
    # country = "中国"
    def __init__(self, name, age, country):
        # 实例属性(对象属性)
        self.name = name
        self.age = age
        self.country = country
