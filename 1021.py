N, K = map(int, input().split())
arr = list(map(int, input().split()))
arr2 = []
arr3 = []
arr4 = []
answer = 0
for i in arr:
    if i in arr4:
        continue
    else:
        arr4.append(i)
        x = arr.count(i)
        arr2.append([i, x])

for i in arr:
    for j in range(len(arr2)):
        if i == arr2[j][0]:

            if len(arr3) < N:
                arr3.append(i)
                arr2[j][1] -= 1
                break
            elif i in arr3:
                arr2[j][1] -= 1
                break
            else:
                arr2.sort(key=lambda x: x[1])
                x = arr3.index(arr2[0][0])
                arr3[x] = i
                answer += 1
                arr2[j][1] -= 1
                break
print(answer)
