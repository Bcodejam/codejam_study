from collections import deque


N, K = map(int, input().split())

queueList = []

#이름 길이는 최대 20이므로
for _ in range(21) :
    queueList.append(deque())

answer = 0

for record in range(N) :
    nameLength = len(input())
    if len(queueList[nameLength]) == 0 :
        queueList[nameLength].append(record)
    else :
        if record - queueList[nameLength][-1] <= K :
            while record - queueList[nameLength][0] > K :
                queueList[nameLength].popleft()
            answer += len(queueList[nameLength])
            queueList[nameLength].append(record)

print(answer)

