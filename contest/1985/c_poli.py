for i in range(int(input())):
    n=int(input())
    a=list(map(int,input().split()))
    mx=0
    summ=0
    c=0
    for i in range(n):
        summ+=a[i]
        mx=max(mx,a[i])
        smx=summ-mx
        if smx==mx:
            c+=1
    print(c)