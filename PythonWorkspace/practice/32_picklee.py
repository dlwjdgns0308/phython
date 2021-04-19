import pickle
profile_file = open("profile.pickle","wb") #피클을 쓰려면 wb로 해야하고 인코딩 설정해줄 필요 없다,
profile = {"이름":"박명수", "나이":30, "취미":["축구","골프","코딩"]}
print(profile)
pickle.dump(profile_file) #profile 에 있는 정보를 file 에 저장
profile_file.close()

# profile_file = open("profile.pickle","wb")
# profile = pickle.load(profile_file) # file 에 있는 정보를 profile 에 불러오기
# print(profile)
# profile_file.close()