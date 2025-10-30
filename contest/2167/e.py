for _ in range(int(input())):
    n, k, x = map(int, input().split())
    a_set = set(map(int, input().split()))
    a_list = sorted(a_set)

    def get_min_len(a, i):
        """Возвращает расстояние от точки i до ближайшей ai
        a должен быть отсортррован"""

        if i <= a[0]:
            return a[0] - i
        
        if i >= a[-1]:
            return i - a[-1]
        
        ai_left, ai_right = 0, len(a) - 1
        while ai_right - ai_left > 1:
            if a[ai_left] == i or a[ai_right] == i:
                return 0

            med = (ai_right + ai_left) // 2
            if a[med] == i:
                return 0

            if a[ai_left] < i < a[med]:
                ai_right = med
            elif a[med] < i < a[ai_right]:
                ai_left = med

        return min(i - a[ai_left], a[ai_right] - i)

    data = {
        0: 0 if 0 in a_set else get_min_len(a_list, 0),
        x: 0 if x in a_set else get_min_len(a_list, x),
    }
    result = set()

    for ai in range(len(a_list) - 1):
        med = (a_list[ai] + a_list[ai + 1]) // 2
        if med not in data:
            data[med] = 0 if med in a_set else get_min_len(a_list, med)

    for ki in range(k):
        max_key = max(data, key=data.get)
        result.add(max_key)
        
        key_left = max_key - 1
        if key_left >= 0 and key_left not in result and key_left not in data:
            data[key_left] = 0 if key_left in a_set else get_min_len(a_list, key_left)
        
        key_right = max_key + 1
        if key_right <= x and key_right not in result and key_right not in data:
            data[key_right] = 0 if key_right in a_set else get_min_len(a_list, key_right)
        
        del data[max_key]
    
    print(*sorted(result))