# 4963
import heapq
from copy import deepcopy
from collections import deque
answer = []

dy = [1, 0, -1, 0, 1, -1, -1, 1]
dx = [0, 1, 0, -1, 1, -1, 1, -1]


def bfs(graph, y, x, w, h):
    q = deque()
    q.append((y, x))
    while q:
        y, x = q.popleft()
        graph[y][x] = 2
        for i in range(8):
            if y+dy[i] >= h or x+dx[i] >= w or y+dy[i] < 0 or x+dx[i] < 0:
                continue
            if graph[y+dy[i]][x+dx[i]] == 2:
                continue
            if graph[y+dy[i]][x+dx[i]] == 1:
                graph[y+dy[i]][x+dx[i]] = 2
                q.append((y+dy[i], x+dx[i]))


while 1:
    w, h = map(int, input().split())
    if w == 0 and h == 0:
        for i in answer:
            print(i)
        break
    answer.append(0)
    graph = []
    for _ in range(h):
        graph.append(list(map(int, input().split())))
    for i in range(h):
        for j in range(w):
            if graph[i][j] == 1:
                bfs(graph, i, j, w, h)
                answer[-1] += 1
# 2583
M, N, K = map(int, input().split())
graph = [[0]*N for _ in range(M)]
for _ in range(K):
    a, b, c, d = map(int, input().split())
    for i in range(b, d):
        for j in range(a, c):
            graph[i][j] = 1
answer = []
px = [0, 1, 0, -1]
py = [1, 0, -1, 0]


def bfs(graph, y, x, answer):
    q = deque()
    q.append((y, x))
    while q:
        dy, dx = q.popleft()

        for i in range(4):
            if dx+px[i] >= N or dx+px[i] < 0 or dy+py[i] >= M or dy+py[i] < 0:
                continue
            if graph[dy+py[i]][dx+px[i]] == 1:
                continue
            q.append((dy+py[i], dx+px[i]))
            graph[dy+py[i]][dx+px[i]] = 1
            answer[-1] += 1


for i in range(M):
    for j in range(N):
        if graph[i][j] == 0:
            answer.append(1)
            bfs(graph, i, j, answer)
answer.sort()
print(len(answer))
for i in range(len(answer)):
    if answer[i] == 1:
        print(answer[i], end=" ")
    else:
        print(answer[i]-1, end=" ")

# 7569
M, N, H = map(int, input().split())
cube = [[]for i in range(N)]
for i in range(H):
    cube.append(i)
    for j in range(N):
        cube[i].append(list(map(int, input().split())))
answer = 1
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]


def bfs(cube, h, y, x, answer):
    q = deque()
    q.append((h, y, x))
    while q:
        h, y, x = q.popleft()
        answer = cube[h][y][x]+1
        for i in range(4):
            if y+dy[i] < 0 or y+dy[i] >= N or x+dx[i] < 0 or x+dx[i] >= M:
                continue
            if cube[h][y+dy[i]][x+dx[i]] == 0:
                q.append((h, y+dy[i], x+dx[i]))
                cube[h][y+dy[i]][x+dx[i]] = answer
        if h+1 < H and cube[h+1][y][x] == 0:
            q.append((h+1, y, x))
            cube[h+1][y][x] = answer
        if h-1 >= 0 and cube[h-1][y][x] == 0:
            q.append((h-1, y, x))
            cube[h-1][y][x] = answer


for h in range(H):
    for n in range(N):
        for m in range(M):
            if cube[h][n][m] == 1:
                bfs(cube, h, n, m, answer)

for h in range(H):
    for n in range(N):
        if 0 in cube[h][n]:
            answer = 0
            break
        a = max(cube[h][n])
        answer = max(a, answer)
print(answer-1)

# 10026
N = int(input())
graph1 = []
graph2 = []
arr = []
for _ in range(N):
    arr = list(input())
    graph1.append(arr)

graph2 = deepcopy(graph1)


answer1 = 0
answer2 = 0
dy = [1, 0, -1, 0]
dx = [0, 1, 0, -1]


def dfs(graph, C, y, x):
    q = deque()
    q.append((y, x))
    graph[y][x] = 'X'
    while q:
        y, x = q.popleft()

        for i in range(4):
            if y+dy[i] < 0 or y+dy[i] >= N or x+dx[i] < 0 or x+dx[i] >= N:
                continue
            if graph[y+dy[i]][x+dx[i]] == C:
                q.append((y+dy[i], x+dx[i]))
                graph[y+dy[i]][x+dx[i]] = 'X'


def dfs2(graph, C, y, x):

    q = deque()
    q.append((y, x))
    graph[y][x] = 'X'
    while q:
        y, x = q.popleft()
        for i in range(4):
            if y+dy[i] < 0 or y+dy[i] >= N or x+dx[i] < 0 or x+dx[i] >= N:
                continue
            if C == 'R' or C == 'G':
                if graph2[y+dy[i]][x+dx[i]] == 'R' or graph2[y+dy[i]][x+dx[i]] == 'G':
                    q.append((y+dy[i], x+dx[i]))
                    graph2[y+dy[i]][x+dx[i]] = 'X'
            if graph[y+dy[i]][x+dx[i]] == C:
                q.append((y+dy[i], x+dx[i]))
                graph2[y+dy[i]][x+dx[i]] = 'X'


for i in range(N):
    for j in range(N):
        if graph1[i][j] == 'R':
            dfs(graph1, 'R', i, j)
            answer1 += 1
        if graph1[i][j] == 'B':
            dfs(graph1, 'B', i, j)
            answer1 += 1
        if graph1[i][j] == 'G':
            dfs(graph1, 'G', i, j)
            answer1 += 1
        if graph2[i][j] == 'R':
            dfs2(graph2, 'R', i, j)
            answer2 += 1
        if graph2[i][j] == 'B':
            dfs2(graph2, 'B', i, j)
            answer2 += 1
        if graph2[i][j] == 'G':
            dfs2(graph2, 'G', i, j)
            answer2 += 1

print(answer1, answer2)

# 7562
N = int(input())
dy = [-2, -2, -1, -1, 2, 1, 2, 1]
dx = [1, -1, 2, -2, -1, -2, 1, 2]


def bfs(graph, y, x):
    q = deque()
    q.append((y, x))
    graph[y][x] = 0
    while q:
        y, x = q.popleft()
        step = graph[y][x] + 1
        for i in range(8):
            if y+dy[i] < 0 or y+dy[i] >= l or x+dx[i] < 0 or x+dx[i] >= l:
                continue
            if graph[y+dy[i]][x+dx[i]] > step:
                graph[y+dy[i]][x+dx[i]] = step
                q.append((y+dy[i], x+dx[i]))


answer = []
for i in range(N):
    answer.append(0)
    l = int(input())
    graph = [[999]*l for _ in range(l)]
    y, x = map(int, input().split())
    sy, sx = map(int, input().split())
    bfs(graph, y, x)
    answer[-1] = graph[sy][sx]

for i in answer:
    print(i)
# 16236
N = int(input())
size = 2
answer = 0
graph = []
gmap = [[0]*N for _ in range(N)]
for i in range(N):
    arr = list(map(int, input().split()))
    graph.append(arr)
    if 9 in arr:
        x = arr.index(9)
        y = i
dy = [1, 0, -1, 0]
dx = [0, -1, 0, 1]


def min_step(graph, gmap, y, x):
    q = deque()
    q.append((y, x))
    gmap[y][x] = 1000
    while q:
        y, x = q.popleft()
        if gmap[y][x] == 1000:
            step = 1
        else:
            step = gmap[y][x]+1
        for i in range(4):
            if x+dx[i] >= N or x+dx[i] < 0 or y+dy[i] >= N or y+dy[i] < 0:
                continue
            if graph[y+dy[i]][x+dx[i]] <= size and gmap[y+dy[i]][x+dx[i]] == 0:
                gmap[y+dy[i]][x+dx[i]] = step
                q.append((y+dy[i], x+dx[i]))


hq = []
stack = 0
min_step(graph, gmap, y, x)
graph[y][x] = 0
while 1:
    for i in range(N):
        for j in range(N):
            if graph[i][j] < size and graph[i][j] != 0 and gmap[i][j] != 0:
                step = gmap[i][j]
                heapq.heappush(hq, (step, i, j))
    if len(hq) == 0:
        print(answer)
        break
    step, ny, nx = heapq.heappop(hq)
    answer += step
    while hq:
        heapq.heappop(hq)

    stack += 1
    graph[ny][nx] = 1000
    if size == stack:
        size += 1
        stack = 0

    gmap = [[0]*N for _ in range(N)]
    min_step(graph, gmap, ny, nx)
    graph[ny][nx] = 0
# 3055
R, C = map(int, input().split())
graph = []
wq = []
wy = True
wx = True
wq = deque()
for i in range(R):
    arr = list(input())
    if '*' in arr:
        for j in range(len(arr)):
            if arr[j] == '*':
                wy = i
                wx = j
                wq.append((wy, wx))
    if 'S' in arr:
        y = i
        x = arr.index('S')
    if 'D' in arr:
        fy = i
        fx = arr.index('D')
    graph.append(arr)
dy = [1, 0, -1, 0]
dx = [0, 1, 0, -1]

q = []


def bfs(graph, y, x):
    q = deque()
    q.append((y, x))
    step = 0
    flag = False
    while q or wq:
        for _ in range(len(wq)):
            wy, wx = wq.popleft()
            for i in range(4):
                py = wy+dy[i]
                px = wx+dx[i]
                if py < 0 or px < 0 or py >= R or px >= C:
                    continue
                # if graph[py][px] == 'S':
                   ## graph[py][px] = '*'
                    ##flag = True
                if graph[py][px] == '.':
                    graph[py][px] = '*'
                    wq.append((py, px))
        if flag:
            break
        for _ in range(len(q)):
            y, x = q.popleft()
            if graph[y][x] == 'S':
                graph[y][x] = int(0)
                step = 1
            else:
                step = graph[y][x] + 1
            for i in range(4):
                py = y+dy[i]
                px = x+dx[i]
                if py < 0 or px < 0 or py >= R or px >= C:
                    continue
                if graph[py][px] == '.' or graph[py][px] == 'D':
                    graph[py][px] = step
                    q.append((py, px))


bfs(graph, y, x)

if graph[fy][fx] == 'D':
    print('KAKTUS')
else:
    print(graph[fy][fx])
