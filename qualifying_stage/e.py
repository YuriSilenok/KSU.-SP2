s1 = {1,2,3,3,4}
s2 = {2,3,4,5}
print(s1 - s2)


n, m = map(int, input().split())
reb = []
for _ in range(m):
    nodes= tuple(map(int, input().split()))
    reb.append(nodes)
print(reb)
