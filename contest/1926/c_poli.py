maxn = 200000
 
digit = [0] * (maxn + 1)
pref = [0] * (maxn + 1)
 
for i in range(1, maxn + 1):
    digit[i] = digit[i // 10] + (i % 10)
    pref[i] = pref[i - 1] + digit[i]
 
t = int(input())
for _ in range(t):
    n = int(input())
    print(pref[n])