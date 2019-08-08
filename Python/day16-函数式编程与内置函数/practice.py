# num_1=[1,2,3,4,5,6,7]
# ret=[]
# for i in num_1:
#     ret.append(i**2)
# print(ret)
#
# def map_test(array):
#     ret=[]
#     for i in array:
#         ret.append(i**2)
#     return ret
# ret=map_test(num_1)
# print(ret)
#
# def map_test(func,array):
#     ret=[]
#     for i in array:
#         res=func(i)
#         ret.append(res)
#     return ret
# print(map_test(lambda x:x+1,num_1))
# msg="tasdfast"
# print(list(map(lambda x:x.upper(),msg)))

# movie_people=["1_sb","2_sb","3_sb","4","5","6"]
# print(list(filter(lambda x:not x.endswith("sb"),movie_people)))

from functools import reduce
num_1=[1,2,3,100]
print(reduce((lambda x,y:x+y),num_1,9))
