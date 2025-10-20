for _ in range(int(input())):
    x, y, k = map(int, input().split())
    
    kx = x // k
    if x % k != 0:
        kx += 1
    
    ky = y // k
    if y % k != 0:
        ky += 1
    
    if kx > ky:
        ky += kx - ky - 1
    else:
        kx += ky - kx
    
    print(kx + ky)