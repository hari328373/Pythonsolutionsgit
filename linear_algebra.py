import numpy
arr=[list(map(float,input().split())) for _ in range(int(input()))]
print(numpy.linalg.det(arr),2)
