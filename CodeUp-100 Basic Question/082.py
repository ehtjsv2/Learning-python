#별표 #출력 후 줄바꿈말고 다른 것으로 바꾸기
a=int(input())
for i in range(1,a+1):
    if((i%10)%3==0 and i%10>0):
        print("X",end=' ')
    else:
        print(i,end=' ')