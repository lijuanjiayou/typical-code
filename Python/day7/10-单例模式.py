
# 单例模式 在程序中这个类创建出来的对象 只有一个(也就是占用一份内存地址)
# 单例模式 也只会走一次__init__方法(保证这个单例对象的属性也是唯一的)(name=小明 age=20)
# 合理的使用内存(避免内存浪费)
class Person(object):

    # 定义一个类属性  保存这个类创建的对象
    __instance = None
    # 定义一个类属性 判断是否是第一次走init方法
    __is_first = True
    # 创建对象
    # 重写new方法 是为了完成单例模式中的对象地址唯一
    def __new__(cls, *args, **kwargs):
        # 判断是否通过这个类创建过对象
        # 如果没有值需要创建
        if not cls.__instance:
            # 创建对象保存起来
            cls.__instance = object.__new__(cls)

        # 如果有值直接返回
        return cls.__instance

    def __init__(self, name, age):
        # 判断是否是第一次
        if Person.__is_first:
            # 赋值一次
            self.name = name
            self.age = age
            # 设置类属性is_first 为False
            Person.__is_first = False

    # def make(self):
    #
    #     hm = HMTest()
    #     hm.my_func(20, 30)


# 创建对象
xiaoming = Person("小明", 20)
print(xiaoming.name)
xiaohong = Person("小红", 21)
print(xiaohong.name)
xiaoyang = Person("小阳", 22)
print(xiaoyang.name)
#
print(xiaoming.name, xiaohong.name, xiaoyang.name)


# num = None
# # 如果不为none 也就是真
# if not num:
#     print("测试")


# 单例的好处???
class HMTest(object):
    def my_func(self, a, b):
        return a + b


# 在程序中 需要计算多次求和操作 比如1000次 可以省掉999分内存
# 每次使用
# 实例化一个对象
# hm = HMTest()
# hm.my_func(10, 20)

# 为了节约内存

