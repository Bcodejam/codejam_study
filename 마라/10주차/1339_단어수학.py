N = int(input())

#dict에 A:1000 B :110 이런식으로 비중을 저장
d = dict()

for _ in range(N):
    string = input()
    for i in range(len(string)) :
        ch = string[i]
        if ch in d:
            d[ch] += 10 ** (len(string) - i)
        else :
            d[ch] = 10 ** (len(string) - i)
#비중이 높은 순서대로 sort
sorted_d = sorted(d.items() , key = lambda item : item[1], reverse=True)

answer = 0    
num = 9

# 비중에 9 8 7 6... 순서대로 곱해주기
for ch, i in sorted_d :
    answer += num *(i//10)
    num -= 1

print(answer)