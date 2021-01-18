from collections import deque
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
