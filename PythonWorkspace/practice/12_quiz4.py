from random import *
comment = list(range(1, 21))
print(comment)
luck = sample(comment, 4)
print("-- 당첨자 발표 --")
print("치킨 당첨자 : {0}".format(luck[0]))
print("커피 당첨자 : {0}".format(luck[1:]))