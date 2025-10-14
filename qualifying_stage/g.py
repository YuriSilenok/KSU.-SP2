from collections import Counter

s = input()
t = input()
i1 = 0
i2 = len(t) - 1
s_len = len(s)
dict_for_t = Counter(t)
dict_for_s = Counter(s[i1:(i2+1)])
# for t_char in t:
#     d[t_char] = d.get(t_char, 0) + 1

done = False
while True:
    if dict_for_t == dict_for_s:
        print(i1+1)
        done = True
        break
    

    if i2+1 >= s_len:
        break

    # dict_for_s[s[i1]] = dict_for_s[s[i1]] - 1
    dict_for_s[s[i1]] -= 1
    i2 += 1
    dict_for_s[s[i2]] = dict_for_s.get(s[i2], 0) + 1
    if dict_for_s[s[i1]] == 0:
        del dict_for_s[s[i1]]
    i1 += 1

if not done:
    print(0)
    

