cabinet = {"A-3":"유재석","B-100":"김태호"}
print(cabinet["A-3"])
print(cabinet["B-100"])

# 새 손님
cabinet["A-3"] = "김종국"
cabinet["C-20"] = "조세호"
print(cabinet)

del cabinet["A-3"]
print(cabinet)

#key 들만 출력
print(cabinet.keys())
print(cabinet.values())
print(cabinet.items())

# 폐점
cabinet.clear()
print(cabinet)


