#별표 #이차원배열만들기
d=[]
for i in range(20):
    d.append([])
    for j in range(20):
        d[i].append(0)
n=int(input())
a=0
b=0
for i in range(n):
    a,b=input().split()
    a=int(a)
    b=int(b)
    d[a][b]=1
for i in range(20):
    for j in range(20):
        print(d[i][j],end=' ')
    print()