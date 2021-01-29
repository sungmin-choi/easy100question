# 10816
import sys
N = int(sys.stdin.readline())
arr = list(sys.stdin.readline().split())
M = int(sys.stdin.readline())
arr2 = list(sys.stdin.readline().split())


def BS(arr, target):
    start = 0
    end = len(arr)-1
    while start <= end:
        mid = (start+end) // 2
        if arr[mid] == target:
            return arr[start:end+1].count(target)
        elif arr[mid] > target:
            end = mid-1
        elif arr[mid] < target:
            start = mid + 1


arr.sort()
dic = {}
for i in arr:
    if i not in dic:
        dic[i] = BS(arr, i)

print(' '.join(str(dic[x]) if x in dic else '0' for x in arr2))
