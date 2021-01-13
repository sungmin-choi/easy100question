import sys
N, K = map(int, input().split())
number = sys.stdin.readline()
answer = []
p = 0
L = K
index = 0
i = 0
while len(answer) < N-K:
    if int(number[i]) > p:
        p = int(number[i])
        index = i
    if i == L:
        answer.append(str(p))
        i = index+1
        L += 1
        p = 0
    else:
        i += 1


print(''.join(answer))
