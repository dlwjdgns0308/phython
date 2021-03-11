temp = int(input("기온이 어때요?"))
if 30 <= temp:
    print("너무더우니 나가지마세요")
elif 10 <= temp and temp < 30:
    print("괜찮은 날씨에요")
elif 0 <= temp < 10:
    print("외투를 챙기세요")
else:
    print("너무 추우니 나가지 마세요")