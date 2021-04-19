C = int(input())
result = 0
b = 0
for i in range(C):
    num = list(map(int, input()))
    a = num[0]
    del num[0]
    for j in num:
        j = j / a
        result = result + j
    for k in num    
    if k <= result:
        del num[b]
        b += 1
    else:
        b += 1
    g = count(num) / a
    print(g)