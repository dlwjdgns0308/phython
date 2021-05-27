# 정규식
import re
# abcd, book, desk
#ca?e
#care, cafe, cave


p = re.compile("ca.e")
# (ca.e) : 하나의 문자를 의미 > care, cafe, case(o) | caffe(x)
# (^de) : 문자열의 시작 > desk, destination(o) | fade(x)
# (se$) : 문자열의 끝 > case, base (o) | face(x)

def print_match(m):
    if m:
        print("m.group():",m.group()) # 일치하는 문자열 반환
        print(m.string) #입력받은 문자열
        print(m.start()) #일치하는 문자열의 시작 index
        print(m.end()) #일치하는 문자열의 끝 index
        print(m.span()) #일치하는 문자열의 시작과 끝 index
    else:
        print("매칭되지 않음")

#m = p.match("case") # match: 주어진 문자열의 처음부터 일치하는지 확인
#print_match(m)
#print(m.group()) # 매치되지 않으면 에러가 발생

#m = p.search("good care") #search : 주어진 문자열 중에 일치하는게 있는지 확인
#print_match(m)

lst = p.findall("good care cafe") # findall : 일치하는 모든 것을 리스트 형태로 반환
print(lst)