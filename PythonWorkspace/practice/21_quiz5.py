from random import *
ctn = 0
call = [range(50)]
for song in range(1, 51) :
    time = randint(1, 50)
    if 5 <= time <= 15 :
        print("[O] {0}번째 손님 (소요시간 : {1}분)".format(song,time))
        ctn += 1
    else :
        print("[ ] {0}번째 손님 (소요시간 : {1}분)".format(song,time))
print("총 탑승 승객 : {0}분 ".format(ctn))
