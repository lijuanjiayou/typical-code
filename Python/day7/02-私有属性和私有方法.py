# # 自定义一个师傅类
# class Master(object):
#
#     # 构造方法
#     def __init__(self):
#         # 配方
#         self.kongfu = "古法配方"
#         # 添加一个属性
#         # 如果一个属性的名字开头是两个下划线 就代表这个属性私有
#         self.__money = 10000
#
#     # 制作煎饼果子
#     def make_cake(self):
#         print("古法煎饼果子赚了%d元" % self.__money)
#         # 在类的里面是可以使用的
#         # print(self.__money)
#         # self.__hello_python()
#
#
#     # 私有的实例方法
#     # 高大尚
#     def __hello_python(self):
#         print("我爱python")
#

# # # 自定义一个对象
# # lishifu = Master()
# # print(lishifu.kongfu)
# # # 如果一个属性私有后 那么就不能使用对象调用这个属性(类的外面使用)
# # # print(lishifu.__money)
# # lishifu.make_cake()
# # # 对象不能调用私有的方法
# # # lishifu.__hello_python()

# 自定义一个师傅类
class Master(object):

    # 构造方法
    def __init__(self):
        # 配方
        self.kongfu = "古法配方"
        # 添加一个属性
        # 如果一个属性的名字开头是两个下划线 就代表这个属性私有
        self.__money = 10000


    # 制作煎饼果子
    def make_cake(self):
        print("古法煎饼果子")


    # 私有的实例方法
    # 高大尚
    def __hello_python(self):
        print("我爱python")


# 自定义一个类 继承师傅类
class Prentice(Master):
    pass


damao = Prentice()
print(damao.kongfu)
damao.make_cake()
# "子类继承了父类 如果父类的属性或者方法私有后 将不会被继承"


