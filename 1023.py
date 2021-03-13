from collections import deque

begin = "hit"
target = "cog"
words = ["cog", "hot", "dot", "dog", "lot", "log", "hot"]
answer = 0
t = 1
visited = [0]*len(words)
begin = list(begin)
q = deque()
q.append((begin, 0))
while q:
    qword, t = q.popleft()
    t = t+1
    i = 0
    i2 = 0
    for idx, word in enumerate(words):
        word = list(word)

        count = 0
        count2 = 0
        for c in word:
            if c not in qword:
                count += 1
                i = idx
        for c in qword:
            if c not in word:
                count2 += 1
                i2 = idx
        if count == 1:
            if visited[i] == 0:
                visited[i] = t
                q.append((word, t))
        elif count2 == 1:
            if visited[i2] == 0:
                visited[i2] = t
                q.append((word, t))


for i in range(len(words)):
    if target == words[i]:
        answer = visited[i]
        break
print(answer)
