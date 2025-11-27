t = int(input())
for _ in range(t):
    n=int(input())
    summa=0
    for i in range(1, n+1):
        if i < 10:
            summa += i
        else:
            for j in str(i):
                summa += int(j)
    print(summa)