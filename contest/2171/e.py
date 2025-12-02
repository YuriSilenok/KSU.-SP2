def solve():
    n = int(input())
    a2 = []
    a3 = []
    ax = []
    for i in range(1, n+1):
        if i % 2 == 0:
            a2.append(i)
        elif i % 3 == 0:
            a3.append(i)
        else:
            ax.append(i)
    while (len(ax) > 0 and len(a2) > 1):
        print(ax.pop(), end=' ')
        print(a2.pop(), end=' ')
        print(a2.pop(), end=' ')
    while (len(ax) > 0 and len(a3) > 1):
        print(ax.pop(), end=' ')
        print(a3.pop(), end=' ')
        print(a3.pop(), end=' ')
    for i in a2:
        print(i, end=' ')
    for i in a3:
        print(i, end=' ')
    for i in ax:
        print(i, end=' ')
for _ in int(input()):
    solve()
    
