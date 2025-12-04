for _ in range(int(input())):
    n = int(input())
    reh_p = "##"
    dot_p = ".."
    strok1 = strok2 = ""
    for i in range(n):
        if i % 2 == 0:
            strok1 += reh_p
            strok2 += dot_p
        else:
            strok1 += dot_p
            strok2 += reh_p
    
    for i in range(n):
        if i % 2 == 0:
            print(strok1 + "\n" + strok1)
        else:
            print(strok2 + "\n" + strok2)