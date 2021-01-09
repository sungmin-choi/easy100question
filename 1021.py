
import sys
T = int(input())
answer = []
for i in range(T):
    arr1 = []
    arr2 = []
    N = int(input())
    for _ in range(N):
        a, b = map(int, sys.stdin.readline().strip().split())
        flag = True
        for j in range(len(arr1)):
            if a < arr1[j] and b < arr2[j]:
                arr1.remove(arr1[j])
                arr2.remove(arr2[j])
            elif a > arr1[j] and b > arr2[j]:
                flag = False
        if flag:
            arr1.append(a)
            arr2.append(b)
    answer.append(len(arr1))

for i in range(T):
    print(answer[i])
