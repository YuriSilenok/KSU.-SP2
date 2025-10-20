# from collections import Counter

# s = input()
# t = input()
# i1 = 0
# i2 = len(t) - 1
# s_len = len(s)
# dict_for_t = Counter(t)
# dict_for_s = Counter(s[i1:(i2+1)])
# # for t_char in t:
# #     d[t_char] = d.get(t_char, 0) + 1

# done = False
# while True:
#     if dict_for_t == dict_for_s:
#         print(i1+1)
#         done = True
#         break
    

#     if i2+1 >= s_len:
#         break

#     # dict_for_s[s[i1]] = dict_for_s[s[i1]] - 1
#     dict_for_s[s[i1]] -= 1
#     i2 += 1
#     dict_for_s[s[i2]] = dict_for_s.get(s[i2], 0) + 1
#     if dict_for_s[s[i1]] == 0:
#         del dict_for_s[s[i1]]
#     i1 += 1

# if not done:
#     print(0)


# from collections import Counter

# s = input()
# t = input()

# s_len = len(s)
# i1 = 0
# i2 = len(t) - 1

# if len(t) > s_len:
#     print(0)
# else:
#     dict_for_t = Counter(t)
#     dict_for_s = Counter(s[i1:i2+1])

#     for i1 in range(s_len - len(t) + 1):
#         i2 = i1 + len(t) - 1
#         if dict_for_s == dict_for_t:
#             print(i1 + 1)
#             break

#         if i2 + 1 < s_len:
#             dict_for_s[s[i1]] -= 1
#             if dict_for_s[s[i1]] == 0:
#                 del dict_for_s[s[i1]]
#             dict_for_s[s[i2 + 1]] = dict_for_s.get(s[i2 + 1], 0) + 1
#     else:
#         print(0)

