for _ in range(int(input())):
    n, m  = map(int, input().split())
    count_max = 0
    res_i = None
    res_j = None

    for i in range(n):
        row = input()
        count = row.count('#')
        if count > count_max:
            res_i = i
            count_max = count
        if count == 1:
            res_j = row.index('#')
    
    print(res_i+1, res_j+1)