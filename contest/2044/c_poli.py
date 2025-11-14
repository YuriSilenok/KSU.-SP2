t = int(input())
for _ in range(t):
    otvet = 0
    ost = 0
    m,a,b,c = map(int, input().split(sep=' '))
    for x in (a, b):
        if m>=x:
            otvet += x
            ost += m-x
        else:
            otvet += m

    if ost>=c:
        otvet +=c
    else:
        otvet += ost
    print(otvet)