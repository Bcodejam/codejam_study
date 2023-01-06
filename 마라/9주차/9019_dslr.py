from collections import deque

N = int(input())


for _ in range(N) :
    visited = [False for _ in range(10000)]
    q = deque()
    A , B = map(int, input().split())
    #dslr 경로와 숫자 저장
    q.append(['', A])

    while q :
        dslr , num = q.popleft()
        visited[num] = True
        if num == B :
            print(dslr)
            break
        #D
        newNum = (2 * num) % 10000
        if not visited[newNum] :
            q.append([dslr + "D", newNum])
            visited[newNum] = True

        #S
        if num == 0 :
            newNum = 9999
        else :
            newNum = num - 1
        if not visited[newNum] :
            q.append([dslr + "S", newNum])
            visited[newNum] = True
        
        #L
        newNum = (num % 1000) * 10 + (num // 1000)
        if not visited[newNum] :
            q.append([dslr + "L", newNum])
            visited[newNum] = True 

        #R
        newNum = (num % 10) * 1000 + num // 10
        if not visited[newNum] :
            q.append([dslr + "R", newNum]) 
            visited[newNum] = True


        

        
    



