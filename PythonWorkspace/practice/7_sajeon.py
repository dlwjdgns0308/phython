cabinet = {3:"유재석", 100:"김태호"}
print(cabinet[3])
print(cabinet[100])

print(cabinet.get(3))

#print(cabinet[5]) 오류나고 프로그램끝남
print(cabinet.get(5)) 
print(cabinet.get(5,"사용 가능")) #집어 넣는거 x, 5번 값이 없으면 사용가능 출력 
print("hi")

print(3 in cabinet)
print(5 in cabinet)
