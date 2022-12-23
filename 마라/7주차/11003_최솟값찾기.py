from collections import deque

N, L = map(int, input().split())
lst = map(int, input().split())

q = deque()

m = 1000000000

m2 = 1000000000

answerlst = []

for item in lst :
    q.append(item)
    #큐에 L 길이 이상 원소가 들어갈 경우
    if len(q) > L  :
        if q[0] == m :
            m = m2
        q.popleft()
        
    
    if item <= m :
        m = item
    else :
        if item > m and item <= m2 :
            m2 = item
    
    answerlst.append(m)


print(answerlst)

    