# 杨辉三角：
def triangles():
    L = [1]
    while 1:
        yield L
        L=[1]+[L[i] + L[i+1] for i in range(len(L)-1)]+[1]


x=0
for t in triangles():
    print (t)
    x = x + 1
    if x ==100:
        break









