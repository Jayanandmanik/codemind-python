import math
x,y,M=map(int,input().split())
a=int(math.pow(x,y)%M)
print(a)