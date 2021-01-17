# 4963
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
