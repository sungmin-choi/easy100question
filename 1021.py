
N, K = map(int, input().split())
num = list(input())
result, dk = [], K
for i in range(N):
    while dk > 0 and result:
        if result[-1] < num[i]:
            result.pop()
            dk -= 1
        else:
            break

    result.append(num[i])
print(''.join(result[:N-K]))
