t = int(input())
for _ in range(t):
    a, b = input().split()
    A = b[0] + a[1:]
    B = a[0] + b[1:]
    print(A, B)