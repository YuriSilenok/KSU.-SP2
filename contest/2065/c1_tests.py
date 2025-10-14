def generate_test_cases():
    test_cases = []

    # Базовые случаи с n=1
    for n in [1]:
        for m in [1]:
            for a1 in [1, 2]:
                for b1 in [1, 2]:
                    test_cases.append((n, m, [a1], b1))

    # Случаи с n=2, m=1
    for n in [2]:
        for m in [1]:
            for a1 in [1, 2, 3]:
                for a2 in [1, 2, 3]:
                    for b1 in [1, 2, 3]:
                        test_cases.append((n, m, [a1, a2], b1))

    # Случаи с n=3, m=1
    for n in [3]:
        for m in [1]:
            for a1 in [1, 2, 3, 4]:
                for a2 in [1, 2, 3, 4]:
                    for a3 in [1, 2, 3, 4]:
                        for b1 in [1, 2, 3, 4]:
                            test_cases.append((n, m, [a1, a2, a3], b1))

    # Добавляем больше разнообразия
    for n in [2, 3]:
        for m in [1, 2]:
            for b1 in [1, 2, 3, 4, 5]:
                # Генерируем разные комбинации a
                if n == 2:
                    for a1 in range(1, 4):
                        for a2 in range(1, 4):
                            test_cases.append((n, m, [a1, a2], b1))
                else:  # n == 3
                    for a1 in range(1, 3):
                        for a2 in range(1, 3):
                            for a3 in range(1, 3):
                                test_cases.append((n, m, [a1, a2, a3], b1))

    return test_cases


def print_test_cases(x):
    test_cases = generate_test_cases()
    print(len(test_cases))

    xn = 1
    for n, m, a_list, b in test_cases:
        if xn == x:
            print(f"***{xn}***")
            print(f"{n} {m}")
            print(" ".join(map(str, a_list)))
            print(b)
        xn += 1


x = int(input("введите номер тестового случая: "))
# Генерируем тестовые данные
print_test_cases(x)
