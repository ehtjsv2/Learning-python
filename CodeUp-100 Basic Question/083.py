a,b,c=input().split()
a=int(a)
b=int(b)
c=int(c)
n=0
for i in range(a):
    for j in range(b):
        for k in range(c):
            print(i,j,k)
            n=n+1
print(n)