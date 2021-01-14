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
