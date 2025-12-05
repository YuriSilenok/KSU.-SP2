for _ in range(int(input())):
    n = int(input())
    s = list(map(int,input().split()))
    mx1, mx2 = sorted(s, reverse = True)[:2]
    for i in s:
        if i == mx1:
            print(i - mx1, end = " ")
        else:
            print(i - mx2, end = " ")
    print()

for _ in range(int(input())):
    s = list(map(int,input().split(sep=' ')))
    s.sort()
    print(s[1])

for i in range(int(input())):
    a, b , c  = map(int, (input().split()))
    if a < b and a > c or a < c and a > b:
        print(a)
    if b < a and b > c or b < c and b > a:
        print(b)
    if c < b and c > a or c < a and c > b:
        print(c)
          
    