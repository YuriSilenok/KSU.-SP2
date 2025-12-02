def solve():
    n = int(input())
    p = list(map(int, input().split()))
    pre = []
    suf = []
    for i in range(1, n):
        pre.append(min(pre[i-1], p[i]))
    for i in range(n-2, -1, -1):
        suf.append(max(suf[i+1], ))
        


for _ in range(int(input())):
    solve()