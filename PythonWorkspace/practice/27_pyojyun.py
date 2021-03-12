import sys

print("Python","Java","JavaScript", sep=" vs ")
print("Python","Java", sep=",", end="?")
print("무엇이 더 재밌을까요?")

print("Python","Java", file=sys.stdout)
print("Python","Java", file=sys.stderr)

scores = {"수학":0,"영어":50, "코딩":100} #"key":values
for subject, score in scores.items():
    print(subject.ljust(8), str(score).rjust(4), sep=",") #ljust(8) : 8칸만들고 왼쪽정렬

for num in range(1, 21):
    print("대기번호 : " + str(num).zfill(3)) # 001, 002 처럼 3칸으로 나타냄

