from collections import deque
import sys
S = sys.stdin.readline()
stack = []
answer = []
temp = 0
flag = True
solution = 0
for i in S:
    if i == ')':
        if len(stack) > 0:
            if stack[-1] == '(':
                stack.pop()
                j = answer[-1]
                while j != '(':
                    temp += j
                    answer.pop()
                    j = answer[-1]
                answer.pop()
                if temp == 0:
                    answer.append(2)
                else:
                    answer.append(2*temp)
                temp = 0
            else:
                flag = False
                break
        else:
            flag = False
            break
    elif i == ']':
        if len(stack) > 0:
            if stack[-1] == '[':
                stack.pop()
                j = answer[-1]
                while j != '[':
                    temp += j
                    answer.pop()
                    j = answer[-1]
                answer.pop()
                if temp == 0:
                    answer.append(3)
                else:
                    answer.append(3*temp)
                temp = 0
            else:
                flag = False
                break
        else:
            flag = False
            break
    elif i == '(':
        stack.append('(')
        answer.append('(')
    elif i == '[':
        stack.append('[')
        answer.append('[')
if flag:
    for i in answer:
        if i == '(' or i == '[':
            solution = 0
            break
        solution += int(i)
    print(solution)
else:
    print(0)

# 14891
q = [0]*5
q[1] = deque(list(map(int, input())))
q[2] = deque(list(map(int, input())))
q[3] = deque(list(map(int, input())))
q[4] = deque(list(map(int, input())))

N = int(input())
qq = deque()
for _ in range(N):
    a, b = map(int, input().split())
    qq.append((a, b))

while qq:
    a, b = qq.popleft()
    step = 1
    if a == 1:
        for i in range(1, 4):
            if q[i][2] != q[i+1][6]:
                step += 1
            else:
                break
        for j in range(step):
            q[a].rotate(b)
            b = -b
            a += 1
    elif a == 2:
        if q[a-1][2] != q[a][6]:
            q[a-1].rotate(-b)
        for i in range(2, 4):
            if q[i][2] != q[i+1][6]:
                step += 1
            else:
                break
        for j in range(step):
            q[a].rotate(b)
            b = -b
            a += 1
    elif a == 3:
        if q[a+1][6] != q[a][2]:
            q[a+1].rotate(-b)
        for i in range(3, 1, -1):
            if q[i][6] != q[i-1][2]:
                step += 1
            else:
                break
        for j in range(step):
            q[a].rotate(b)
            b = -b
            a -= 1
    elif a == 4:
        for i in range(4, 1, -1):
            if q[i][6] != q[i-1][2]:
                step += 1
            else:
                break
        for j in range(step):
            q[a].rotate(b)
            b = -b
            a -= 1
answer = 0

for i in range(1, 5):
    if q[i][0]:
        if i == 1:
            answer += 1
        elif i == 2:
            answer += 2
        elif i == 3:
            answer += 4
        elif i == 4:
            answer += 8

print(answer)
