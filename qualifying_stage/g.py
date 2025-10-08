s = input()
t = input()
i = 0
l = len(s)
while i < l:
    t1 = t
    i2 = i
    while len(t1) > 0 and s[i2] in t1:
        t1 = t1.replace(s[i2], '', 1)
        i2 += 1
    if len(t1) == 0:
        print(i+1)
        break
    i += 1
else:
    print(0)