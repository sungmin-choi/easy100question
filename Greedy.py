# bj2839
import sys
a = int(input())
answer = 0
while 1:
    if a % 5 == 0:
        answer += a // 5
        break
    elif a < 3:
        answer = -1
        break
    elif a == 3:
        answer += 1
        break
    else:
        a = a-3
        answer += 1


print(answer)
# bj1931
n = int(input())
array = []
answer = 1
for _ in range(n):
    a, b = map(int, input().split())
    array.append([a, b])
array.sort(key=lambda x: (x[1], x[0]))
t = array[0][1]
for i in range(1, len(array)):
    if array[i][0] < t:
        continue
    else:
        t = array[i][1]
        answer += 1

print(answer)

# bj5585
n = int(input())
arr = [500, 100, 50, 10, 5, 1]
answer = 0
n = 1000-n
for i in arr:
    if n == 0:
        break
    if n >= i:
        answer += (n//i)
        n = n-(n//i)*i
print(answer)

# bj2217

n = int(input())
arr = []
for _ in range(n):
    arr.append(int(input()))

arr.sort(reverse=True)
answer = arr[0]
for i in range(len(arr)):
    if i+1 < len(arr):
        answer = max(answer, arr[i+1]*(i+2))
print(answer)

# 1946
T = int(input())
answer = []
for i in range(T):
    arr = []

    N = int(input())
    for _ in range(N):
        a, b = map(int, sys.stdin.readline().strip().split())
        arr.append((a, b))
    arr.sort(key=lambda x: x[0])
    answer.append(0)
    c, d = 0, 0
    for j in range(len(arr)):
        if 1 in arr[j]:
            answer[i] += 1
            c, d = arr[j]
        elif arr[j][0] < c or arr[j][1] < d:
            answer[i] += 1
            c, d = arr[j]

for i in range(T):
    print(answer[i])
