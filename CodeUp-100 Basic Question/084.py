a,b,c,d=input().split()
a=int(a)
b=int(b)
c=int(c)
d=int(d)
e=a*b*c*d
e=float(e)
print(format(e/8.0/1024.0/1024.0,".1f"),"MB")