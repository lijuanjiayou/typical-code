
# 自定义类
class Person(object):

    # 私有的类属性(国籍)
    __country = "中国"

    # 构造方法
    def __init__(self):

        self.name = "小明"
        # 私有
        self.__age = 20


    # 实例方法(对象方法)获取私有属性
    def get_age(self):
        return self.__age

    # 实例方法(对象方法)修改私有属性
    def set_age(self, new_age):
        self.__age = new_age

    # 类方法
    # 获取私有类属性
    @classmethod
    def get_country(cls):
        return cls.__country

    # 类方法
    # 修改私有类属性
    @classmethod
    def set_country(cls, new_country):
        cls.__country = new_country

    # 静态方法
    @staticmethod
    def hello():
        print("今天天气不错")


# 使用静态方法
# 01: 类名.静态方法名
# Person.hello()

# 02: 对象名.静态方法名
xiaoming = Person()
xiaoming.hello()

# 实例方法
# xiaoming.get_country()

# Person.get_age(Person())

"""
python中类中的方法总结:

- 实例方法(对象方法) -> 场景很多
    - 定义格式: def 实例方法名(self):
    - 调用格式: 对象名.实例方法名()
    - 使用场景: 在方法中需要self
    
- 类方法-> 对私有类属性取值或者赋值
    - 定义格式: @classmethod
                def 类方法名(cls):
    - 调用格式: 类名.类方法名() 或者 对象名.类方法名()
    - 使用场景: 在方法中需要cls(类名)
    
- 静态方法 -> 一般不用
    - 定义格式: @staticmethod
                def 静态方法名():
    - 调用格式: 类名.类方法名() 或者 对象名.类方法名()
    - 使用场景: 在方法中不需要self  也不需要cls
    
"""










