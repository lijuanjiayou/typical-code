"""
try:
    执行可能发生异常的代码01(不同的异常类型)
    执行可能发生异常的代码02(不同的异常类型)
except (异常类型1, 异常类型2,...):
    如果发生异常执行的代码
"""
# print(num)
try:
    # 可能有异常
    open("hm.txt", "r")

    print(num)
except (FileNotFoundError, NameError):
    print("捕获到异常了")
