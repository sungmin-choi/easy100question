# bj2839
from collections import deque
import heapq
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
# 개인적으로 어려웠음 이런 계산 방법 떠오르지 않았다 다시끔 되새김질 하길
n = int(input())
s = list(map(int, input().split()))
s.sort()
num = 1
for i in range(n):
    if num < s[i]:
        break
    num += s[i]
print(num)

# 1783
N, M = map(int, sys.stdin.readline().split())
answer = 1
if N == 1:
    answer = 1
if N == 2:
    if M >= 7:
        answer = 4
    else:
        answer = 1+(M-1)//2
if N >= 3 and M == 1:
    answer = 1
if N >= 3 and M == 2:
    answer = 2
if N >= 3 and M == 3:
    answer = 3
if N >= 3 and M >= 4:
    if M < 7:
        answer = 4
    elif M >= 7:
        answer = M-2

print(answer)

# 1449
N, L = map(int, input().split())

arr = list(map(int, input().split()))

arr.sort()
i = 0
answer = 1
c = arr[0]
while i < N:
    if L >= arr[i]+1-c:
        i += 1
    else:
        c = arr[i]
        answer += 1
        i += 1

print(answer)

# 1202
N, K = map(int, input().split())
gem = []
for _ in range(N):
    weight, value = map(int, sys.stdin.readline().split())
    heapq.heappush(gem, [weight, value])
bag = []
for _ in range(K):
    capacity = int(sys.stdin.readline())
    heapq.heappush(bag, capacity)

answer = 0
capable_gem = []
for _ in range(K):
    capacity = heapq.heappop(bag)
    while gem and capacity >= gem[0][0]:
        [weight, value] = heapq.heappop(gem)
        heapq.heappush(capable_gem, -value)
    if capable_gem:
        answer -= heapq.heappop(capable_gem)
    elif not gem:
        break

print(answer)

# 1700
N, K = map(int, input().split())
arr = list(map(int, input().split()))
answer = 0
arr2 = [0]*(K+1)
arr3 = []
for i in arr:
    if arr2[i] == 0:
        arr2[i] = arr.count(i)

for i in arr:
    if len(arr3) < N:
        if i in arr3:
            arr2[i] -= 1
        else:
            arr3.append(i)
            arr2[i] -= 1
    elif i in arr3:
        arr2[i] -= 1
    else:
        p = arr3[0]
        for j in range(len(arr3)):
            if j+1 < len(arr3):
                if arr2[p] > arr2[arr3[j+1]]:
                    p = arr3[j+1]
        x = arr3.index(p)
        arr3[x] = i
        arr2[i] -= 1
        answer += 1

print(answer)

# 1439
S = input()
answer0 = 0
answer1 = 0
if int(S[0]) == 0:
    answer1 = 1
else:
    answer0 = 1

p = int(S[0])
for i in range(1, len(S)):
    if p == int(S[i]):
        continue
    else:
        if int(S[i]) == 1:
            p = 1
            answer0 += 1
        else:
            p = 0
            answer1 += 1
answer = min(answer0, answer1)
print(answer)

# 2847
N = int(input())
arr = []
for _ in range(N):
    arr.append(int(input()))

answer = 0
for i in range(len(arr)-1, 0, -1):
    if i-1 >= 0:
        if arr[i] <= arr[i-1]:
            while arr[i] <= arr[i-1]:
                arr[i-1] -= 1
                answer += 1
print(answer)

# 10775
G = int(input())
P = int(input())
parent = []
for i in range(G+1):
    parent.append(i)

plane = []
for _ in range(P):
    plane.append(int(input()))


def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]


def union(parent, x, y):
    a = find_parent(parent, x)
    b = find_parent(parent, y)
    parent[a] = b


answer = 0
for i in plane:
    x = find_parent(parent, i)
    if x == 0:
        break
    union(parent, x, x-1)
    answer += 1

print(answer)

# 13305
N = int(input())
distance = list(map(int, sys.stdin.readline().split()))
q = []
cityOil = list(map(int, sys.stdin.readline().split()))
q = deque(cityOil)
cheap = min(cityOil)
a = sum(distance)
answer = 0
i = 0
cost = q.popleft()
while len(q) > 1:
    cost2 = q.popleft()
    if cost > cost2:
        answer += cost*distance[i]
        cost = cost2
        i += 1
    else:
        answer += cost*distance[i]
        i += 1
answer += cost*distance[i]
print(answer)

# 1715

N = int(input())
answer = 0
q = []
for _ in range(N):
    heapq.heappush(q, int(input()))
p2 = 0
p1 = 0
answer = 0
while len(q) > 1:
    p1 = heapq.heappop(q)
    if q:
        p2 = heapq.heappop(q)
        heapq.heappush(q, p1+p2)
        answer += p1+p2
    else:

        heapq.heappush(q, p1)

print(answer)
# 2820
N = int(input())
seat = input()
l = len(seat)
answer = 1
q = []
q = deque(seat)
while q:
    s = q.popleft()
    if s == "S":
        answer += 1
    elif s == "L":
        q.popleft()
        answer += 1
if answer > l:
    answer = l
print(answer)
# 2812

N, K = map(int, input().split())
num = list(input())
result, dk = [], K
for i in range(N):
    while dk > 0 and result:
        if result[-1] < num[i]:
            result.pop()
            dk -= 1
        else:
            break

    result.append(num[i])
print(''.join(result[:N-K]))
