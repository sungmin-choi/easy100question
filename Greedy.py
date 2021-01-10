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

# 1339

N = int(input())
array = []
alphabet = [0]*26
answer = 0
for _ in range(N):
    array.append(input())

for word in array:
    for i in range(len(word)):
        alphabet[ord(word[i])-65] += 10**(len(word)-i-1)

alphabet.sort(reverse=True)

count = 9
for i in alphabet:
    if i == 0:
        break
    else:
        answer += i*count
        count -= 1

print(answer)

# 1138
N = int(input())
INF = 9999
array = list(map(int, input().split()))
answer = [INF]*N

c = 1
cnt = 0
for i in array:
    for j in range(N):

        if cnt == i and answer[j] == INF:
            answer[j] = c
            break
        if answer[j] > c:
            cnt += 1
    c += 1
    cnt = 0

for i in answer:
    print(i, end=" ")
# 1744
N = int(input())

array = []
plus = []
minus = []
for _ in range(N):
    array.append(int(input()))

array.sort(reverse=True)
for i in array:
    if i > 1:
        plus.append(i)
    else:
        minus.append(i)

plus.sort(reverse=True)
minus.sort()
answer = 0
i = 0
while i < len(plus):
    if plus[i] > 1 and i+1 < len(plus) and plus[i+1] > 1:
        answer += plus[i]*plus[i+1]
        i += 2
    else:
        answer += plus[i]
        i += 1
i = 0
while i < len(minus):
    if minus[i] < 0 and i+1 < len(minus) and minus[i+1] < 0:
        answer += minus[i]*minus[i+1]
        i += 2
    elif minus[i] < 0 and i+1 < len(minus) and minus[i+1] == 0:
        answer += minus[i]*minus[i+1]
        i += 2
    else:
        answer += minus[i]
        i += 1

print(answer)

# 4796

arr2 = []
arr = []
flag = True
while flag:
    L, P, V = map(int, input().split())
    if L == 0 and P == 0 and V == 0:
        flag = False
    else:
        arr.append([L, P, V])

for l, p, v in arr:
    answer = 0
    answer += (v//p)*l
    v = v-(v//p)*p
    if v < l:
        answer += v
    else:
        answer += l
    arr2.append(answer)

for i in range(len(arr2)):
    print("Case "+str(i+1)+": "+str(arr2[i]))


# 2437
