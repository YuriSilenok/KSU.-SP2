t = int(input())

for _ in range(t):
    s = input()

    for i in range(len(s)-1):
        if s[i] != s[i+1]:
            s_new = s[:i]+s[i+1]+s[i]

            if i < len(s)-2:
                s_new += s[i+2:]
            
            print('YES')
            print(s_new)
            break

    else:
        print('NO')        

