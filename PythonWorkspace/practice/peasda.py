N = int(input())
sum = 0
for i in range(N):
    inssa = str(input())
    assa = list(inssa)
    for j in assa:
            ke = inssa.find(j)
            assa.remove(j)
            ge = inssa.find(j) + 1
            if ke + 1 != ge:
                if ge == 0:
                    sum = sum +1
            else:
                sum = sum + 1
print(sum)







