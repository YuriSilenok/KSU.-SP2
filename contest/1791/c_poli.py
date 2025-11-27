for _ in range(int(input())):
    n = int(input())
    s = input()
    i = 0
    c = n // 2
    while i < c:
        if s[i] == s[-i-1]:
            break
        i += 1
    print(n - i * 2)