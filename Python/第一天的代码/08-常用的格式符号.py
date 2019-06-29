
# 业务需求:定义四个变量
# 名字:小明 年龄:30身高: 180.1 是否是男性:否
# 全部使用命名规则为下划线
# 名字
my_name = "小明"
# 年龄
my_age = 30
# 身高
my_height = 180.1
# 是否是男性
is_man = True

# 依次输出内容:
# 我的名字:小明
# %s 等于str -> string
print("我的名字:%s" % my_name)
# 我的年龄:30岁
# %d 等于digit
print("我的年龄:%d岁" % my_age)
# 我的身高:180.1cm
# 默认情况下 python使用%f 会保留小数点后面六位
# %f 等于 float
print("我的身高:%.2f" % my_height)

# 如果想打印一个bool值 如果想显示True 或者 False 要使用%s
# 如果想显示1 或者 0 要使用%d
# 是否是男性: False
print("是否是男性:%s" % is_man)
# 是否是男性: 0
print("是否是男性:%d" % is_man)

