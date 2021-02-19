#문자열
sentence = '나는 소년입니다'
print(sentence)
sentence2 = """
나는 소년이고,
파이썬은
굉장히
쉽답니다
"""
print(sentence2)

#슬라이스 자르기
jumin = "990120-1234567"
print("성별 : " + jumin[7])
print("연 : " + jumin[0:2]) #0부터 2 직전까지 (0,1)
print("월  : " + jumin[2:4])
print("일 : " + jumin[4:6])

print("생년월일 : "  + jumin[:6])
print("뒤 7자리 : " + jumin[7:])
print("뒤 7자리 (뒤에서부터) : " + jumin[-7:])
#맨뒤에서 7번쨰부터 끝까지


#문자열2
python = "Python is Amazing"
print(python.lower())
print(python.upper())
print(python[0].isupper())
print(len(python))
print(python.replace("Python","Java")) #Python이란 단어를 Java로 바꿈
index = python.index("n")#n이 몇번째에 있니
print(index)
index = python.index("n", index + 1)
print(index)

print(python.find("Java"))

print(python.count("n")) 


#문자열 포맷
print("a"+"b")
print("a","b")

#방법1
print("나는%d살입니다." % 20) #정수 
print("나는%s을 좋아해요" %"파이썬") #문자열
print("Apple 은 %c로 시작해요" % "A") #문자

print("나는 %s 색과 %s색을 좋아해요" %("파란","빨간"))

#방법2
print("나는 {}살 입니다.".format(20))
print("나는 {}색과 {}색을 좋아해요".format("파란","빨간"))
print("나는 {1}색과 {0}색을 좋아해요".format("파란","빨간"))


#방법3
#print("나는 {age}살이며, {color}색을 좋아해요.".format(age=20, color="빨간"))

#방법 4
age = 20
color = "빨간"
print(f"나는 {age}살이며, {color}색을 좋아해요.")