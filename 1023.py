
numbers = [2, 20, 200]
answer = ''
maxl = len(str(max(numbers)))
numbers = list(map(str, numbers))
arr = []
for i in range(len(numbers)):
    l = maxl-len(numbers[i])
    number = numbers[i]
    for j in range(l):
        number += number[0]
    arr.append((number, i))

arr.sort(key=lambda x: -int(x[0]))
for i in arr:
    answer += str(numbers[i[1]])
if answer[0] == "0":
    answer = "0"

print(answer)
