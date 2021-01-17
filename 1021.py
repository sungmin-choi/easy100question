from collections import deque
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
