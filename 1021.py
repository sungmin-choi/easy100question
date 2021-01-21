from collections import deque
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
