
# try嵌套

# try:
#     try:
#         open("hm1.txt", "r")
#     finally:
#         print("里面的finally")
# except:
#     print("捕获到了异常")



# def my_func1():
#     print(num)
#
# def my_func2():
#     my_func1()
#
# def my_func3():
#     my_func2()
#
# try:
#     my_func3()
# except:
#     print("异常")


# def my_func1():
#     print(num)
#
# def my_func2():
#     my_func1()
#
# def my_func3():
#     try:
#         my_func2()
#     except:
#         print("异常")
#
# my_func3()


# def my_func1():
#     print(num)
#
# def my_func2():
#     try:
#         my_func1()
#     except:
#         print("异常")
#
# def my_func3():
#     my_func2()
#
# my_func3()



def my_func1():
    # 请写这种方式
    try:
        print(num)
    except:
        print("异常")

def my_func2():
    my_func1()

def my_func3():
    my_func2()

my_func3()


# 捕获异常是可以传递的