for _ in range(int(input())):
    a1, a2, b1, b2 = map(int, input().split())
    s = 0
    sch_1 = sch_2 = 0
    for a, b in zip((a1,a2), (b1, b2)):
        if a > b:
            sch_1 += 1
        elif a < b:
            sch_2 += 1
        else:
            sch_1 += 0.5
            sch_2 += 0.5
    if sch_1 > sch_2:
        s += 1

    sch_1 = sch_2 = 0
    for a, b in zip((a1,a2), (b2, b1)):
        if a > b:
            sch_1 += 1
        elif a < b:
            sch_2 += 1
        else:
            sch_1 += 0.5
            sch_2 += 0.5
    if sch_1 > sch_2:
        s += 1

    print(s * 2)