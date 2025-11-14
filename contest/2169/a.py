for _ in range(int(input())):
    n, a = map(int, input().split())
    l = list(map(int, input().split()))

    if a < l[0]:
        print(a + 1)
        continue

    for li in range(n):
        if l[li] > a:
            if li - l.count(a) >= n - li:
                print(a - 1)
            else:
                print(a + 1)
            break
    else:
        print(a - 1)