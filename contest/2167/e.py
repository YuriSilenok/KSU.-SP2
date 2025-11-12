t = int(input())
for _ in range(t):
    n, k, x = map(int, input().split())
    a_set = set(map(int, input().split()))
    
    # Преобразуем множество в отсортированный список и добавляем границы
    a = sorted({0} | a_set | {x})
    n = len(a)
    
    l, r = 0, x + 1
    while l + 1 < r:
        m = (l + r) // 2
        f = 0
        # Временно изменяем границы для подсчета
        temp_a0 = a[0]
        temp_an1 = a[n-1]
        a[0] = -m
        a[n-1] = x + m
        
        for i in range(1, n):
            gap = (a[i] - m) - (a[i-1] + m) + 1
            f += max(0, gap)
        
        # Восстанавливаем оригинальные значения
        a[0] = temp_a0
        a[n-1] = temp_an1
        
        if f >= k:
            l = m
        else:
            r = m
    
    # Устанавливаем финальные границы
    a[0] = -l
    a[n-1] = x + l
    
    j = 0
    output = []
    for i in range(1, n):
        start = max(j, a[i-1] + l)
        end = min(a[i] - l, x)
        while start <= end and k > 0:
            output.append(str(start))
            start += 1
            k -= 1
        j = start
        if k == 0:
            break
    
    print(" ".join(output))