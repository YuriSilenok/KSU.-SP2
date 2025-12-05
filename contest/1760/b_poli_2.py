t = int(input())
for _ in range(t):
    n = int(input())
    s = str(input())
    a = ord(max(s, key=ord))
    print(a-ord('a')+1)