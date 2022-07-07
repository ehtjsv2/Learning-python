a,b,c=input().split()
a=int(a)
b=int(b)
c=int(c)
e=a*b*c
e=float(e)
print(format(e/8.0/1024.0/1024.0,".2f"),"MB")