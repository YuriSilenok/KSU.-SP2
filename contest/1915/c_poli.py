t=int(input())
for _ in range(t):
    n=int(input())
    s=sum(map(int,input().split()))
    r=int(s**0.5)
    if r*r==s:
        print("YES")
    else:
        print("NO")


