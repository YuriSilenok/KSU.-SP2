rep = {
    'p': 'q',
    'q': 'p',
    'w': 'w'
}

for _ in range(int(input())):
    a=list(input())
    a.reverse()
    for i, ch in enumerate(a):
        a[i] = rep[ch]
    
    print(''.join(a))