n=int(input())
a=input().split()
min=10001
for i in range(n):
    a[i]=int(a[i])
    if(a[i]<min):
        min=a[i]
print(min)