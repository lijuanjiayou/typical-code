


try:
    open("hm1.txt", "r")

except:
    # try中的代码发生了异常执行except代码
    print("except")
else:
    # 如果try中的代码没有发生异常 就会执行else中的代码
    print("else")
finally:
    # 无论try中的异常代码是否发生异常 finally都会执行
    print("finally")


try:
    open("hm1.txt", "r")

except:
    # try中的代码发生了异常执行except代码
    print("except")
finally:
    # 无论try中的异常代码是否发生异常 finally都会执行
    print("finally")


# 根本就没有捕获异常 还是会发生异常的(程序崩溃)
try:
    open("hm1.txt", "r")

finally:
    # 无论try中的异常代码是否发生异常 finally都会执行
    print("finally")