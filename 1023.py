for i in range(R):
    for j in range(C):
        graph2.append([i, j])
        for k in range(4):
            y, x = i+dy[k], j+dx[k]
            if y >= R or x >= C or y < 0 or x < 0:
                continue
            graph2[-1].append(graph[y][x])
answer = 1
def dfs(graph2, stack):
