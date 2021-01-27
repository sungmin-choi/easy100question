import sys
from collections import deque
N, M = map(int, sys.stdin.readline().split())
graph = []
pq = deque()
graph2 = [[0]*M for _ in range(N)]
for _ in range(N):
    graph.append(list(map(int, sys.stdin.readline().split())))

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

num = 1


def bfs(y, x, graph2, num):
    q = deque()
    q.append((y, x))
    while q:
        y, x = q.popleft()
        graph2[y][x] = num
        for i in range(4):
            Y, X = y+dy[i], x+dx[i]
            if Y < 0 or Y >= N or X < 0 or X >= M:
                continue
            if graph[Y][X] != 0 and graph2[Y][X] == 0:
                graph2[Y][X] = num
                q.append((Y, X))


answer = 0
while num == 1:
    for i in range(N):
        for j in range(M):
            if graph[i][j] != 0:
                t = 0
                for k in range(4):
                    y, x = i+dy[k], j+dx[k]
                    if y < 0 or y >= N or x < 0 or x >= M:
                        continue
                    if graph[y][x] == 0:
                        t += 1
                pq.append((i, j, t))
    while pq:
        y, x, t = pq.popleft()
        if graph[y][x] >= t:
            graph[y][x] -= t
        else:
            graph[y][x] = 0

    answer += 1
    for i in range(N):
        for j in range(M):
            if graph[i][j] != 0 and graph2[i][j] == 0:
                bfs(i, j, graph2, num)
                num += 1
    num -= 1
    graph2 = [[0]*M for _ in range(N)]
if num == 0:
    print(0)
else:
    print(answer)
