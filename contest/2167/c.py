for _ in range(int(input())):
    n = int(input())
    m = list(map(int, input().split()))
    is_sorted = False
    for i in range(1, n):
        if m[0] % 2 != m[i] % 2:
            is_sorted = True
            break
    if is_sorted:
        m.sort()
    print(*m)