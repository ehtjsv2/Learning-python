#별표 #16진수곱
a=input()
a=int(a,16)
for i in range(1,16):
    print('%X'%a,"*%X"%i,"=%X"%(a*i),sep='')