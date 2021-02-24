from itertools import combinations
import copy
from copy import deepcopy
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

# 15683


def input(): return sys.stdin.readline().strip()


answer = 9999999
dy = [0, 0, -1, 1]
dx = [1, -1, 0, 0]
di = [0, [[0], [1], [2], [3]], [[0, 1], [2, 3]], [
    [0, 2], [0, 3], [1, 3], [1, 2]], [[0, 1, 2], [0, 1, 3]], [[0, 1, 2, 3]]]


def dfs(start, graph, cctv):
    global answer
    if start == len(cctv):
        count = 0
        for i in range(N):
            count += graph[i].count(0)
        answer = min(answer, count)
        return
    else:

        y, x, num = cctv[start]
        for k in di[num]:
            temp = deepcopy(graph)
            for i in k:
                ny = y+dy[i]
                nx = x+dx[i]
                while N > ny >= 0 and M > nx >= 0:
                    if temp[ny][nx] == 6:
                        break
                    elif temp[ny][nx] == 0:
                        temp[ny][nx] = '#'
                    ny += dy[i]
                    nx += dx[i]
            dfs(start+1, temp, cctv)


graph = []
N, M = map(int, input().split())
cctv = []
for i in range(N):
    arr = list(map(int, input().split()))
    for j in range(M):
        if arr[j] not in [0, 6]:
            cctv.append((i, j, arr[j]))
    graph.append(arr)

dfs(0, graph, cctv)
print(answer)


input = sys.stdin.readline


dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]
di = [0, [[0], [1], [2], [3]], [[0, 1], [2, 3]], [[1, 2], [1, 3], [0, 2],
                                                  [0, 3]], [[0, 1, 2], [0, 1, 3], [0, 2, 3], [1, 2, 3]], [[0, 1, 2, 3]]]

MIN = 9999999999999999


def dfs(start, MAP, cctv):
    global MIN
    if start == len(cctv):
        cnt = 0
        for y in range(0, row):
            for x in range(0, col):
                if MAP[y][x] == 0:
                    cnt += 1
        MIN = min(MIN, cnt)
        return

    num, y, x = cctv[start]
    for dir in di[num]:
        tmp = copy.deepcopy(MAP)
        for i in dir:
            ny, nx = y+dy[i], x+dx[i]
            while row > ny >= 0 and col > nx >= 0:
                if tmp[ny][nx] == 6:
                    break
                elif tmp[ny][nx] == 0:
                    tmp[ny][nx] = '#'
                ny += dy[i]
                nx += dx[i]
        dfs(start+1, tmp, cctv)


if __name__ == "__main__":
    row, col = map(int, input().split())
    MAP = [list(map(int, input().split())) for _ in range(row)]
    cctv = []

    for y in range(0, row):
        for x in range(0, col):
            if MAP[y][x] not in [0, 6]:
                cctv.append([MAP[y][x], y, x])

    dfs(0, MAP, cctv)
    print(MIN)

    # 3190
    import sys


def input(): return sys.stdin.readline().strip()


apple = []
snake = [[0, 0]]
N = int(input())
map = [[0]*N for _ in range(N)]
K = int(input())

for _ in range(K):
    a, b = input().split()
    apple.append((int(a)-1, int(b)-1))

ride = deque()
L = int(input())

for _ in range(L):
    x, c = input().split()
    ride.append((int(x), c))


dy = [0, -1, 0, 1]
dx = [1, 0, -1, 0]
d = 0
time = 0
flag = True
flag2 = True
while True:
    if flag:
        if ride:
            t, c = ride.popleft()
            flag = False
    y, x = snake[-1]
    nx = x+dx[d]
    ny = y+dy[d]
    flag2 = True
    if 0 <= nx < N and 0 <= ny < N:
        if [ny, nx] not in snake:
            for i in range(len(apple)):
                if ny == apple[i][0] and nx == apple[i][1]:
                    snake.append([ny, nx])
                    apple.remove((ny, nx))
                    flag2 = False
                    break
            if flag2:
                snake.append([ny, nx])
                snake.remove(snake[0])
        else:
            break
    else:
        break
    time += 1
    if time == t:
        if c == 'L':
            if d == 3:
                d = 0
            else:
                d += 1
        elif c == 'D':
            if d == 0:
                d = 3
            else:
                d -= 1
        flag = True

print(time+1)

# 15686


def input(): return sys.stdin.readline().strip()


N, M = map(int, input().split())
home = []  # 집 좌표 저장 리스트
chicken = []  # 치킨집 좌표 저장 리스트
for i in range(N):
    arr = list(map(int, input().split()))
    for j in range(N):
        if arr[j] == 1:
            home.append((i+1, j+1))
        elif arr[j] == 2:
            chicken.append((i+1, j+1))
candidates = list(combinations(chicken, M))
answer = 1e9
for candidate in candidates:
    result = 0
    for hy, hx in home:
        temp = 1e9
        for cy, cx in candidate:
            temp = min(temp, abs(hy-cy)+abs(hx-cx))
        result += temp
    answer = min(result, answer)

print(answer)
# 14499


def tcube(s, cube):
    if s == 1 or s == 2:
        temp1 = cube[1][2]
        temp2 = cube[1][1]
        temp3 = cube[1][0]
        temp4 = cube[3][1]
        if s == 1:
            cube[3][1] = temp1
            cube[1][1] = temp3
            cube[1][0] = temp4
            cube[1][2] = temp2
        else:
            cube[3][1] = temp3
            cube[1][1] = temp1
            cube[1][0] = temp2
            cube[1][2] = temp4
    if s == 3 or s == 4:
        temp1 = cube[0][1]
        temp2 = cube[1][1]
        temp3 = cube[2][1]
        temp4 = cube[3][1]
        if s == 3:
            cube[0][1] = temp2
            cube[1][1] = temp3
            cube[2][1] = temp4
            cube[3][1] = temp1
        else:
            cube[0][1] = temp4
            cube[1][1] = temp1
            cube[2][1] = temp2
            cube[3][1] = temp3


def input(): return sys.stdin.readline().strip()


n, m,  y, x, step = map(int, input().split())
cube = [[0]*3 for _ in range(4)]
graph = []

graph = [list(map(int, input().split())) for _ in range(n)]
arr = list(map(int, input().split()))
stepq = deque(arr)
temp1, temp2, temp3, temp4 = 0, 0, 0, 0
dy = [0, 0, -1, 1]
dx = [1, -1, 0, 0]
while stepq:
    s = stepq.popleft()
    ny = y+dy[s-1]
    nx = x+dx[s-1]
    if 0 <= ny < n and 0 <= nx < m:
        tcube(s, cube)
        if graph[ny][nx] == 0:
            graph[ny][nx] = cube[3][1]
        else:
            cube[3][1] = graph[ny][nx]
            graph[ny][nx] = 0
        y = ny
        x = nx
        print(cube[1][1])


# 14500


def f1(x1, x2, x3, x4, y1, y2, y3, y4, n, m, answer):
    X1, X2, X3, X4 = x1, x2, x3, x4
    for i in range(n):
        y1 += 1
        y2 += 1
        y3 += 1
        y4 += 1
        x1, x2, x3, x4 = X1, X2, X3, X4
        if y1 >= n or y2 >= n or y3 >= n or y4 >= n:
            break
        for j in range(m):
            x1 += 1
            x2 += 1
            x3 += 1
            x4 += 1
            if x4 >= m or x3 >= m or x2 >= m or x1 >= m:
                break
            temp = graph[y1][x1]+graph[y2][x2]+graph[y3][x3]+graph[y4][x4]
            answer = max(answer, temp)
    return answer


def f2(y, x, answer):
    y1, y2, y3, y4, y5, y6 = y-1, y-1, y-1, y, y, y
    x1, x2, x3, x4, x5, x6 = x-2, x-1, x, x-2, x-1, x
    temp = graph[y1][x1]+graph[y2][x2]+graph[y4][x4]+graph[y5][x5]
    answer = max(answer, temp)
    temp = graph[y6][x6]+graph[y2][x2]+graph[y3][x3]+graph[y5][x5]
    answer = max(answer, temp)
    temp = graph[y1][x1]+graph[y2][x2]+graph[y3][x3]+graph[y5][x5]
    answer = max(answer, temp)
    temp = graph[y6][x6]+graph[y2][x2]+graph[y4][x4]+graph[y5][x5]
    answer = max(answer, temp)
    temp = graph[y1][x1]+graph[y2][x2]+graph[y6][x6]+graph[y5][x5]
    answer = max(answer, temp)
    temp = graph[y4][x4]+graph[y2][x2]+graph[y3][x3]+graph[y5][x5]
    answer = max(answer, temp)
    temp = graph[y4][x4]+graph[y6][x6]+graph[y3][x3]+graph[y5][x5]
    answer = max(answer, temp)
    temp = graph[y4][x4]+graph[y6][x6]+graph[y1][x1]+graph[y5][x5]
    answer = max(answer, temp)
    temp = graph[y2][x2]+graph[y6][x6]+graph[y1][x1]+graph[y3][x3]
    answer = max(answer, temp)
    temp = graph[y2][x2]+graph[y4][x4]+graph[y1][x1]+graph[y3][x3]
    answer = max(answer, temp)
    return answer


def f3(y, x, answer):
    y1, y2, y3, y4, y5, y6 = y-2, y-2, y-1, y-1, y, y
    x1, x2, x3, x4, x5, x6 = x-1, x, x-1, x, x-1, x
    temp = graph[y1][x1]+graph[y2][x2]+graph[y3][x3]+graph[y4][x4]
    answer = max(answer, temp)
    temp = graph[y6][x6]+graph[y4][x4]+graph[y3][x3]+graph[y5][x5]
    answer = max(answer, temp)

    temp = graph[y1][x1]+graph[y2][x2]+graph[y3][x3]+graph[y5][x5]
    answer = max(answer, temp)
    temp = graph[y6][x6]+graph[y2][x2]+graph[y4][x4]+graph[y1][x1]
    answer = max(answer, temp)
    temp = graph[y4][x4]+graph[y2][x2]+graph[y6][x6]+graph[y5][x5]
    answer = max(answer, temp)
    temp = graph[y1][x1]+graph[y6][x6]+graph[y3][x3]+graph[y5][x5]
    answer = max(answer, temp)

    temp = graph[y4][x4]+graph[y1][x1]+graph[y3][x3]+graph[y5][x5]
    answer = max(answer, temp)
    temp = graph[y4][x4]+graph[y6][x6]+graph[y2][x2]+graph[y3][x3]
    answer = max(answer, temp)

    temp = graph[y4][x4]+graph[y6][x6]+graph[y1][x1]+graph[y3][x3]
    answer = max(answer, temp)
    temp = graph[y2][x2]+graph[y4][x4]+graph[y5][x5]+graph[y3][x3]
    answer = max(answer, temp)
    return answer


def input(): return sys.stdin.readline().strip()


n, m = map(int, input().split())

graph = [list(map(int, input().split())) for _ in range(n)]
answer = 0
temp = 0
x1, x2, x3, x4 = -1, 0, 1, 2
y1, y2, y3, y4 = -1, -1, -1, -1
answer = f1(x1, x2, x3, x4, y1, y2, y3, y4, n, m, answer)
x1, x2, x3, x4 = -1, -1, -1, -1
y1, y2, y3, y4 = -1, 0, 1, 2
answer = f1(x1, x2, x3, x4, y1, y2, y3, y4, n, m, answer)

for i in range(n):
    y = i+1
    if y < n:
        for j in range(m):
            x = j+2

            if x < m:
                answer = f2(y, x, answer)
            else:
                break
    else:
        break

for i in range(n):
    y = i+2
    if y < n:
        for j in range(m):
            x = j+1

            if x < m:
                answer = f3(y, x, answer)
            else:
                break
    else:
        break


print(answer)


# 16234
def input(): return sys.stdin.readline().strip()


n, l, r = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]
graph2 = [[0]*n for _ in range(n)]
time = 0
dy = [0, 1, 0, -1]
dx = [1, 0, -1, 0]
q = deque()
answer = 0
while True:
    i, j = 0, 0
    temp = 1
    flag = True
    arr = [0]
    for i in range(n):
        for j in range(n):
            if graph2[i][j] == 0:
                time = 1
                sum1 = graph[i][j]
                q.append((i, j))
                while q:
                    y, x = q.popleft()
                    for k in range(4):
                        ny = y+dy[k]
                        nx = x+dx[k]
                        if 0 <= ny < n and 0 <= nx < n:
                            if l <= abs(graph[ny][nx]-graph[y][x]) <= r and graph2[ny][nx] == 0:
                                q.append((ny, nx))
                                graph2[y][x] = temp
                                graph2[ny][nx] = temp
                                sum1 += graph[ny][nx]
                                time += 1
                                flag = False
                if flag:
                    continue
                else:
                    arr.append(int(sum1/time))
                    temp += 1
    for i in range(n):
        for j in range(n):
            if graph2[i][j] != 0:
                graph[i][j] = arr[graph2[i][j]]
    graph2 = [[0]*n for _ in range(n)]

    if flag:
        break
    answer += 1


print(answer)
