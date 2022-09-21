from collections import namedtuple
n=int(input())
colums=list(input().split())
total=0
for _ in range(n):
    total+=int(list(input().split())[colums.index('MARKS')])
print(total/n)

