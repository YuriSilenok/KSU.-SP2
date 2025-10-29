for _ in range(int(input())):
    n, k, x = map(int, input().split())
    a_set = set(map(int, input().split()))
    a_list = sorted(a_set)
    b = set(range(k)) | set(range(x, x - k, -1))
    data = dict()
    for i in range(len(a_list)):

        for ki in range(1, k + 1):
            if a_list[i] - k >= 0:
                b.add(a_list[i] - k)
            if a_list[i] + k <= x:
                b.add(a_list[i] + k)
            s = (a_list[i-1] + a_list[i]) // 2
            b.add(s)
            if i > 0:
                if s - k >= 0:
                    b.add(s - k)
                elif s + k <= x:
                    b.add(s + k)

        
    b = b - a_set

    for bi in b:
        min_len = x
        for ai in a_set:
            if abs(ai - bi) < min_len:
                min_len = abs(ai - bi)
        data[bi] = min_len
    data_key_sort = set(list(sorted(data, key=lambda key: data[key], reverse=True))[:k])
    
    if len(data_key_sort) < k:
       data_key_sort = data_key_sort | set(a_list[:(k - len(data_key_sort))])
    print(*sorted(data_key_sort))


