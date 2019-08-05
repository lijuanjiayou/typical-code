"""
try:
    执行可能发生异常的代码
except 异常类型:
    如果发生异常执行的代码
"""

try:
    open("hm1.txt", "r")
    print("测试")
    print(num)
except FileNotFoundError:
    print("发生异常了")
    # open("hm.txt", "w")

print("往下运行")