N = int(input())
sum = 1
k = 0
a = 1
res = 1
while (a + sum <= N) or (N >= a + sum + k + 6):
    k += 6
    sum = sum + k
    res += 1
print(res)





    