gun = 10

def checkpoint(soldiers): #경계근무
    global gun # 전역 공간에 있는 gun 사용 (원래는 함수 내에서 정의되지 않으면 오류남)
    gun = gun - soldiers
    print("[함수 내] 남은 총 : {0}".fomat(gun))

def checkpoint_ret(gun, soldiers):
    gun = gun - soldiers
    print("[함수 내] 남은 총 : {0}".format(gun))
    return gun
print("전체 총: {0}".format(gun) )
#checkpoint(2)
gun = checkpoint_ret(gun, 2)
print("남은 총: {0}".format(gun) )