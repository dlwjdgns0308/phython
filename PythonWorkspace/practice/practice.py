T = int(input())
chng = 1
ho = 1
for i in range(T):
    H,W,N = map(int, input().split())
    for j in range(N):
        if H > chng:
            chng += 1
        elif H <= chng:
            chng = 1
            ho += 1
    chng = str(chng)
    ho = str(ho)
    print(chng+ "d"+ho)
