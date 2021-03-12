def std_weight(height,gender):
    if gender == "man":
        std = round(height * height * 22, 2)
        print("키 {0}cm 남자의 표준 체중은 {1}kg 입니다.".format(height,std))
    else:
        std = round(height * height * 21, 2)
        print("키 {0}cm 여자의 표준 체중은 {1}kg 입니다.".format(height, std))


std_weight(1.55,"man")