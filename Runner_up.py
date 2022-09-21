n = int(input())
arr = list(map(int, input().split()))
m1 = max(arr)
l = []
for i in arr:
    if i != m1:
        l.append(i)
print(max(l))
