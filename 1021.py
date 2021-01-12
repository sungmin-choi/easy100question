G = int(input())
P = int(input())
parent = []
for i in range(G+1):
    parent.append(i)

plane = []
for _ in range(P):
    plane.append(int(input()))


def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]


def union(parent, x, y):
    a = find_parent(parent, x)
    b = find_parent(parent, y)
    if a < b:
        parent[y] = a
    else:
        parent[x] = b


answer = 0
for i in plane:
    x = parent[i]
    if x == 0:
        break
    union(parent, x, x-1)
    answer += 1

print(answer)
