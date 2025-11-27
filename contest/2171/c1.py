t = int(input())
for _ in range(t):    

    n = int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))

    x = 0
    for num in a:
        x ^= num
    for num in b:
        x ^= num
        
    if not x:
        print("Tie")
        continue
        
    idx = 0
    for i in range(n):
        if a[i] ^ b[i]:
            idx = i
            
    print("Mai" if idx & 1 else "Ajisai")

