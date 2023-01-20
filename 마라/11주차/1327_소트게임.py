from  collections import deque;

N , K = map(int, input().split())

visited = set()

lst = list(map(str , input().split()))

answer = 100
def bfs() :
    global answer 
    global lst
    strlist = ''.join(lst)
    q = deque()
    q.append([strlist, 0])
    visited.add(strlist)
    while q :
        num , depth = q.popleft()
        if num == ''.join(sorted(lst)) :
            answer = min(answer, depth)
        if num not in visited :
            visited.add(num)
            for i in range(len(str(num)) - K) :
                tmp = num[i:i+K][::-1]
                for j in range(K) :
                    num[j] = tmp[j]
                q.append([num, depth+1])
                
bfs()
print(answer)    

       
    
        
        