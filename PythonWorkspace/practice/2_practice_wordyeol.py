python = "Python is Amazing"
print(python.lower()) # 소문자로 출력
print(python.upper()) # 대문자로 출력
print(python[0].isupper()) # 0번쨰가 대문자인지 출력
print(len(python)) # 문자열의 길이를 출력
print(python.replace("Python", "Java")) #Python을 Java로 바꾸어서 출력
index = python.index("n") # 가장먼저 나오는 n의 위치 출력
print(index)
index = python.index("n", index + 1) # 두번째로 나오는 n의 위치 출력
print(index)

print(python.find("Java")) # 없으면 -1 을 출력하고 진행
#print(python.index("Java")) # 없으면 오류나고 프로그램 종료
print(python.count("n")) # n이 몇개 있는지 출력

