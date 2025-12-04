t = int(input())
for _ in range(t):
    a,b,c = map(int, input().split())
    if c == b:
        print(a)
    elif c == a:
        print(b)
    else:
        print(c)