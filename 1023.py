import sys
def input(): return sys.stdin.readline().strip()


answer = []
t = int(input())
for _ in range(t):
    p = input()
    n = int(input())
    de = input()[1:-1].split(',')
    p = p.replace('RR', '')
    r = 1
    f, b = 0, 0
    for i in p:
        if i == 'R':
            r = -r
        elif i == 'D':
            if r == 1:
                f += 1
            else:
                b += 1
    if f+b <= n:
        de = de[f:n-b]

        if r == 1:
            str = "["+','.join(de)+"]"
            answer.append(str)
        else:
            str = "["+','.join(de[::-1])+"]"
            answer.append(str)
    else:
        answer.append("error")


for i in answer:
    print(i)
