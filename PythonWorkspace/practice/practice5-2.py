#사전
cabinet = {3:"유재석", 100: "김태호"}
print(cabinet[3]) #없으면 프로그램 종료

print(cabinet.get(3)) #없으면 None

print(cabinet.get(5,"사용가능"))

print(3 in cabinet) # 3이 있니
print(6 in cabinet)

cabi = {"A-3":"유재석","B-100":"김태호"}
print(cabi["A-3"])


#새 손님
print(cabi)
cabi["A-3"] = "김종국"
cabi["C-20"] = "조세호"
print(cabi)

# 간 손님
del cabi["A-3"]
print(cabi)

# key, value 들만 출력
print(cabinet.keys())
print(cabinet.values())

# 둘다 출력
print(cabi.items())

#목욕탕 폐점
cabi.clear()
print(cabi)