

for _ in range(int(input())):
    n = int(input())
    data = []
    m = 0
    x_count = {}
    for _ in range(n):
        x, y = map(int, input().split())
        data.append((x, y))
        x_count[x] = x_count.get(x, 0) + 1
    x_list = list(x_count)
    m = len(list(filter(lambda key: x_count[key] == 2, x_count)))
    result = (n -2) * m
    for y in (0, 1):
        for x1_ind in range(0, len(x_list) - 1):
            x1 = x_list[x1_ind]
            for x2_ind in range(x1_ind + 1, len(x_list)):
                x2 = x_list[x2_ind]
                if abs(x2 - x1) % 2 == 0:
                    point = (abs(x2 - x1) // 2, 1 if y == 0 else 0)
                    if point in data:
                        result += 1
    print(result)

