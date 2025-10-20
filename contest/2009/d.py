

for _ in range(int(input())):
    n = int(input())
    data = []
    m = 0
    x_count = {}
    y_data = {
        0: set(),
        1: set(),
    }

    for _ in range(n):
        x, y = map(int, input().split())
        y_data[y].add(x)

    y_data_list = {
        0: list(y_data[0]),
        1: list(y_data[1]),
    }

    m = len(y_data[0] & y_data[1])
    result = (n - 2) * m
    for y in (0, 1):
        not_y = 1 if y == 0 else 0
        y_data_len = len(y_data[y])
        for x_ind in range(y_data_len - 1):
            x1 = y_data_list[y][x_ind]
            x2 = None
            for i in (1, 2):
                if x_ind + i < y_data_len and y_data_list[y][x_ind + i] - x1 == 2:
                    x2 = y_data_list[y][x_ind + i]
            if x2 is None:
                continue
            
            if (x1 + 1) in y_data[not_y]:
                result += 1

    print(result)

