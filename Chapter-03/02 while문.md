## 배운점
> * 형태
```py
while 조건:
  ---
  ---
  ---
```
> * break와 continue가 가능하다

## CODE
```py
treeHit = 1
while treeHit:
    treeHit = treeHit+1
    if(treeHit%2!=0):
        continue
    print(treeHit)
    if(treeHit>=100):
        break
```

```
1~100 까지 양수만 출력
```
