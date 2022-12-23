from collections import deque


N, K = map(int, input().split())

queueList = []

#이름 길이는 최대 20이므로 , index 가 길이인 배열 생성
for _ in range(21) :
    queueList.append(deque())

answer = 0

for record in range(N) :
    nameLength = len(input())
    if len(queueList[nameLength]) == 0 :
        queueList[nameLength].append(record)
    else :
        #큐가 비어있지 않고, 큐의 첫번째 원소와 등수차가 K 초과일 경우
        while queueList[nameLength] and record - queueList[nameLength][0] > K :
            #친한 친구가 아니므로 pop
            queueList[nameLength].popleft()
        #남아있는 애들은 친한친구임
        answer += len(queueList[nameLength])
        queueList[nameLength].append(record)
            

print(answer)

