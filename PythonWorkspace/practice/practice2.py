from random import *

print(random()) # 0~1 미만의 임의의 값 생성
print(random()*10)
print(int(random() * 10)) # 0  ~ 10 사이에 임의의 정수값 생성 10 미포함

print(randrange(1, 46)) # 1~46 사이에 임의의 정수값 생성 46 미포함

print(randint(1, 45)) # 1 ~ 45 이하의 임의의 정수값 생성