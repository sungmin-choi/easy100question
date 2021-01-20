from collections import deque
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
