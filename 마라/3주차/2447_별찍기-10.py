def starsList(N) :
  if N==1 :
    return ["*"]
  else : 
    stars = starsList(N//3)
    tmp = []
    #전단계(n//3) 전체 3 번 복사
    for star in stars:
      tmp.append(star * 3)
    #전단계 전체 복사 + 공백 (n//3) + 전단계 전체 복사
    for star in stars:
      tmp.append(star + " " * (N//3) + star)
    #전단계(n//3) 전체 3 번 복사
    for star in stars:
      tmp.append(star * 3) 
    return tmp

n = int(input())
print("\n".join(starsList(n)))