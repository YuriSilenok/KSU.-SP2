t = int(input())

for _ in range(t):
    n = int(input())
    m = []
    for i in range(n):
        string = input()
        f = string.find('#')+1
        m.append(str(f))
    a = m[::-1]
    print(' '.join(a))