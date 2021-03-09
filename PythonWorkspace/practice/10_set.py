my_set = {1,2,3,3,3} # 중복 안됨, 순서 없음
print(my_set)

java = {"유재석","김태호","양세형"}
python = set(["유재석","박명수"])

#교집합(둘다 할수 있는 사람)
print(java & python)
print(java.intersection(python))

# 합집합
print(java | python)
print(java.union(python))

#차집합