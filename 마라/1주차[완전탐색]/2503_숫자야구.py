# index숫자가 답이 가능한경우 0 , 불가능한 경우 1 
lst = [0 for _ in range(0, 1000)]


#question과 testQuestion을 비교하여 스트라이크 , 볼 return
def strikeAndBall(question , testQuestion) :
    question = list(question)
    testQuestion = list(testQuestion)
    strike = 0
    ball = 0
    for i in range(0, 3):
        if question[i] == testQuestion[i] :
            strike += 1 
            question[i] = '0'
            continue
        if question[i] in list(testQuestion) : 
            ball += 1
            question[i] = '0'
    return str(strike) + ' ' + str(ball)


N = int(input())

for _ in range(0, N):
    question, strike, ball = input().split()
    for i in range(123, 1000) : #123 ~ 999까지
        #민혁이가 물어본 question과 민석이의 답(strike + ' ' + ball)으로
        if strike + ' ' + ball != strikeAndBall(question , str(i)) :
            #불가능한 숫자 지우기
            lst[i] = 1

ans = 0

for i in range(123, 1000) :
    #0이 들어가지 않고, 모든 숫자가 중복없고 , 답이될수있는 숫자 count
    if lst[i] == 0 and ('0' not in list(str(i))) and (str(i)[0] != str(i)[1] and str(i)[1] != str(i)[2] and str(i)[0] != str(i)[2]): 
        ans += 1

print(ans)