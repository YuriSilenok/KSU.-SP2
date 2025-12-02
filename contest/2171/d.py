for _ in range(int(input())):
    n = int(input())
    p = list(map(int, input().split()))
    pre = [n] * (n + 1)
    suf = [0] * (n + 1)
    m = n
    for i in range(n):
        pre[i+1] = min(pre[i], p[i])
    for i in range(n-1, -1, -1):
        suf[i] = max(suf[i+1], p[i])
    for i in range(n-1):
        if pre[i+1] > suf[i+1]:
            print("NO")
            break
    else:
        print("YES")