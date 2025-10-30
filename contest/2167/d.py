from math import gcd

for _ in range(int(input())):
    n = int(input())
    a = list(set(map(int, input().split())))

    a_max = max(a)
    x = 2
    while True:
        f2 = False
        for ai in a:
            if gcd(ai, x) == 1:
                f2 = True
                break
        if f2:
            print(x)
            break
        x += 1