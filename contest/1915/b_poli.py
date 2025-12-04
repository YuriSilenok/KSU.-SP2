t = int(input())
for _ in range(t):
    for _ in range(3):
        n=input()
        if '?' in n:
            if "A" not in n:
                print("A")
            elif "B" not in n:
                print("B")
            else:
                print("C")