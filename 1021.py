N = int(input())
arr = list(map(int, input().split()))
arr.sort(reverse=True)
s = sum(arr)
for i in range(1, sum(arr)+1):
    a = i
    p = 0
    flag = True
    for j in arr:
        if a >= j:
            a -= j
        if a == 0:
            flag = False
            break
    if flag:
        print(i)
        break
