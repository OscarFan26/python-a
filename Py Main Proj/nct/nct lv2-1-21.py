L=[[1],[1, 1]]
c=input("输入层数:")
cen=int(c)

def triangles(L,cen):
    n=3
    while n <= cen:
        for i in range(0,n-1):
            L.append([])
            if i==0:
                L[n-1].append(1)
                L[n-1].append(1)
            else:
                L[n-1].insert(i,L[n - 2][i]+L[n - 2][i - 1])
        n=n+1
    return 'done'

triangles(L,cen)

#遍历
for i in range(cen):
    print(L[i])
