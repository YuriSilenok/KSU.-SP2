t = int(input())
for i in range(t):
    n = int(input())
    s = input().strip()
    a = "abcdefghijklmnopqrstuvw"
    max_i = 0
    for j in s:
        i = s.index(j) + 1
        if i > max_i:
            max_i = i
    print(max_i)