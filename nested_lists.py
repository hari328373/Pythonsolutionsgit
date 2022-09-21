d= {}
for _ in range(int(input())):
    name = input()
    score = float(input())
    d[name] = score

v = d.values()
v1 = sorted(list(set(v)))[1]

l = []
for key, value in d.items():
    if value == v1:
        l.append(key)
l = sorted(l)
for i in l:
    print(i)


