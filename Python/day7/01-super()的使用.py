
# 自定义师傅类-古法
class Master(object):

    # 方法
    def make_cake(self):
        print("古法煎饼果子")


# 自定义师傅类-现代
class School(object):

    # 方法
    def make_cake(self):
        print("现代煎饼果子")


# 自定义一个徒弟类
class Prentice(Master, School):

    # 方法
    def make_cake(self):
        print("猫氏煎饼果子")
        Master.make_cake(self)
        School.make_cake(self)

    # 古法
    def make_old_cake(self):
        # 01 方式(单和多继承 都适用)
        # Master.make_cake(self)

        # super默认会调用第一个父类的方法(适用于单继承 或者只想使用第一个父类的方法)

        # 02 方式 适用于新式类
        # 格式: super(子类类名, self).父类方法名()
        # super(Prentice, self).make_cake()

        # 03 方式 (适用于新式类) 02方式的简写
        super().make_cake()

    # 现代
    def make_new_cake(self):
        super().make_cake()



# 自定义一个对象 大猫
damao = Prentice()
# 猫氏
damao.make_cake()
# # 古法
# damao.make_old_cake()
# # 现代
# damao.make_new_cake()