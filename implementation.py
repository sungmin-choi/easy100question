import heapq
from collections import deque
import sys
S = sys.stdin.readline()
stack = []
answer = []
temp = 0
flag = True
solution = 0
for i in S:
    if i == ')':
        if len(stack) > 0:
            if stack[-1] == '(':
                stack.pop()
                j = answer[-1]
                while j != '(':
                    temp += j
                    answer.pop()
                    j = answer[-1]
                answer.pop()
                if temp == 0:
                    answer.append(2)
                else:
                    answer.append(2*temp)
                temp = 0
            else:
                flag = False
                break
        else:
            flag = False
            break
    elif i == ']':
        if len(stack) > 0:
            if stack[-1] == '[':
                stack.pop()
                j = answer[-1]
                while j != '[':
                    temp += j
                    answer.pop()
                    j = answer[-1]
                answer.pop()
                if temp == 0:
                    answer.append(3)
                else:
                    answer.append(3*temp)
                temp = 0
            else:
                flag = False
                break
        else:
            flag = False
            break
    elif i == '(':
        stack.append('(')
        answer.append('(')
    elif i == '[':
        stack.append('[')
        answer.append('[')
if flag:
    for i in answer:
        if i == '(' or i == '[':
            solution = 0
            break
        solution += int(i)
    print(solution)
else:
    print(0)

# 14891
q = [0]*5
q[1] = deque(list(map(int, input())))
q[2] = deque(list(map(int, input())))
q[3] = deque(list(map(int, input())))
q[4] = deque(list(map(int, input())))

N = int(input())
qq = deque()
for _ in range(N):
    a, b = map(int, input().split())
    qq.append((a, b))

while qq:
    a, b = qq.popleft()
    step = 1
    if a == 1:
        for i in range(1, 4):
            if q[i][2] != q[i+1][6]:
                step += 1
            else:
                break
        for j in range(step):
            q[a].rotate(b)
            b = -b
            a += 1
    elif a == 2:
        if q[a-1][2] != q[a][6]:
            q[a-1].rotate(-b)
        for i in range(2, 4):
            if q[i][2] != q[i+1][6]:
                step += 1
            else:
                break
        for j in range(step):
            q[a].rotate(b)
            b = -b
            a += 1
    elif a == 3:
        if q[a+1][6] != q[a][2]:
            q[a+1].rotate(-b)
        for i in range(3, 1, -1):
            if q[i][6] != q[i-1][2]:
                step += 1
            else:
                break
        for j in range(step):
            q[a].rotate(b)
            b = -b
            a -= 1
    elif a == 4:
        for i in range(4, 1, -1):
            if q[i][6] != q[i-1][2]:
                step += 1
            else:
                break
        for j in range(step):
            q[a].rotate(b)
            b = -b
            a -= 1
answer = 0

for i in range(1, 5):
    if q[i][0]:
        if i == 1:
            answer += 1
        elif i == 2:
            answer += 2
        elif i == 3:
            answer += 4
        elif i == 4:
            answer += 8

print(answer)

# AC언어


def input(): return sys.stdin.readline().strip()


answer = []
t = int(input())
for _ in range(t):
    p = input()
    n = int(input())
    de = input()[1:-1].split(',')
    p = p.replace('RR', '')
    r = 1
    f, b = 0, 0
    for i in p:
        if i == 'R':
            r = -r
        elif i == 'D':
            if r == 1:
                f += 1
            else:
                b += 1
    if f+b <= n:
        de = de[f:n-b]

        if r == 1:
            str = "["+','.join(de)+"]"
            answer.append(str)
        else:
            str = "["+','.join(de[::-1])+"]"
            answer.append(str)
    else:
        answer.append("error")


for i in answer:
    print(i)

# 11286


def input(): return sys.stdin.readline().strip()


T = int(input())
q = []
answer = []
for _ in range(T):
    a = int(input())
    if a != 0:
        if a < 0:
            heapq.heappush(q, (-a, -1))
        else:
            heapq.heappush(q, (a, 1))
    else:
        if q:
            c, d = heapq.heappop(q)
            if d < 0:
                answer.append(-c)
            else:
                answer.append(c)
        else:
            answer.append(0)

for i in answer:
    print(i)

# 1713


def input(): return sys.stdin.readline().strip()


N = int(input())
S = int(input())
array = list(map(int, sys.stdin.readline().split()))
q = []
k = 1
for i in array:
    flag = True
    for j in range(len(q)):
        if q[j][2] == i:
            q[j][0] += 1
            q[j][1] = k
            flag = False
            break
    if flag:
        if len(q) == N:
            q.sort(key=lambda x: [x[0], x[1]])
            heapq.heappop(q)
        heapq.heappush(q, [1, k, i])
        k += 1
q.sort(key=lambda x: [x[2]])
for i in range(len(q)):
    print(q[i][2], end=" ")

# 1713


def input(): return sys.stdin.readline().strip()


N = int(input())
S = int(input())
array = list(map(int, sys.stdin.readline().split()))
photo = []

q = []
k = 1
for i in array:
    flag = True
    for j in range(len(q)):
        if q[j][2] == i:
            q[j][0] += 1
            q[j][1] = k
            flag = False
            break
    if flag:
        if len(q) == N:
            q.sort(key=lambda x: [x[0], x[1]])
            heapq.heappop(q)
        heapq.heappush(q, [1, k, i])
        k += 1
q.sort(key=lambda x: [x[2]])
for i in range(len(q)):
    print(q[i][2], end=" ")


def input(): return sys.stdin.readline().strip()


n = int(input())
num = int(input())


def is_in_arr(arr, w):
    for i in arr:
        if i[2] == w:
            return True
    return False


arr = []
who = input().split()
for idx, w in enumerate(who):
    # 1
    if is_in_arr(arr, w):
        # 2
        for index, var in enumerate(arr):
            if var[2] == w:
                arr[index][0] += 1
                break
    else:  # 3
        if len(arr) < n:
            arr.append([1, idx, w])
        else:
            arr[0] = [1, idx, w]
    arr.sort(key=lambda x: (x[0], x[1]))

arr.sort(key=lambda x: int(x[2]))

for i in range(len(arr)):
    if i == n-1:
        print(arr[i][2])
    else:
        print(arr[i][2], end=' ')

# 15686

# 17144


def input(): return sys.stdin.readline().strip()


r, c, t = map(int, input().split())

graph = []
addmap = [[0]*c for _ in range(r)]
aircar = []
for i in range(r):
    arr = list(map(int, input().split()))
    if arr[0] == -1:
        aircar.append((i, 0))
    graph.append(arr)
dy = [1, 0, -1, 0]
dx = [0, 1, 0, -1]
for i in range(t):
    for j in range(r):
        for k in range(c):
            if graph[j][k] > 0:
                p = int(graph[j][k]/5)
                time = 0
                for g in range(4):
                    yy = j+dy[g]
                    xx = k+dx[g]
                    if yy >= 0 and yy < r and xx >= 0 and xx < c:
                        if graph[yy][xx] != -1:
                            addmap[yy][xx] += p
                            time += 1
                addmap[j][k] += -time*p
    for j in range(r):
        for k in range(c):
            graph[j][k] += addmap[j][k]
            addmap[j][k] = 0
    air1 = aircar[0][0]
    air2 = aircar[1][0]
    graph[air1-1][0] = 0
    graph[air2+1][0] = 0
    for j in range(air1-1, 0, -1):
        if j-1 >= 0:
            graph[j][0] = graph[j-1][0]
            graph[j-1][0] = 0
    for j in range(air2+1, r):
        if j+1 < r:
            graph[j][0] = graph[j+1][0]
            graph[j+1][0] = 0
    for j in range(c):
        if j+1 < c:
            graph[0][j] = graph[0][j+1]
            graph[0][j+1] = 0
            graph[r-1][j] = graph[r-1][j+1]
            graph[r-1][j+1] = 0
    for j in range(r-1, air2, -1):
        graph[j][c-1] = graph[j-1][c-1]
        graph[j-1][c-1] = 0
    for j in range(air1):
        graph[j][c-1] = graph[j+1][c-1]
        graph[j+1][c-1] = 0
    for j in range(c-1, 1, -1):
        graph[air1][j] = graph[air1][j-1]
        graph[air1][j-1] = 0
        graph[air2][j] = graph[air2][j-1]
        graph[air2][j-1] = 0

answer = 0
for j in range(r):
    for k in range(c):
        if graph[j][k] != -1 and graph[j][k] != 0:
            answer += graph[j][k]


print(answer)

# 14503


def input(): return sys.stdin.readline().strip()


N, M = map(int, input().split())
r, c, d = map(int, input().split())
graph = []
for _ in range(N):
    graph.append(list(map(int, input().split())))

flag = True
graph[r][c] = 2
answer = 1
dy = [0, -1, 0, 1]
dx = [-1, 0, 1, 0]
by = [1, 0, -1, 0]
bx = [0, -1, 0, 1]
i = 0
while flag:
    yy = r+dy[d]
    xx = c+dx[d]
    if yy >= 0 and yy < N and xx >= 0 and xx < M:
        if i != 4:
            if graph[yy][xx] == 0:
                if d == 0:
                    d = 3
                else:
                    d -= 1
                graph[yy][xx] = 2
                answer += 1
                r = yy
                c = xx
                i = 0
            elif graph[yy][xx] == 1 or graph[yy][xx] == 2:
                i += 1
                if d == 0:
                    d = 3
                else:
                    d -= 1
        else:
            cx = c+bx[d]
            cy = r+by[d]
            if cy >= 0 and cy < N and cx >= 0 and cx < M:
                if graph[cy][cx] != 1:
                    r = cy
                    c = cx
                    i = 0
                else:
                    flag = False

print(answer)
