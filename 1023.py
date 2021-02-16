

from collections import deque
import sys


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
