N, atk = map(int, input().split())
lst = []
answer = 0
for _ in range(N) :
  a = list(map(int, input().split()))
  lst.append(a)

def canClear(Hmax, Hatk) :

  Hcur = Hmax
  for t,a,h in lst :
    if t == 2 :
      Hatk += a
      Hcur = min(Hmax, Hcur + h)
    else :
      #막타 때리면 h//Hatk 만큼의 turn 이 돌아가고
      #막타 못때리면 turn이 한번 더 돌아간다
      turn = h//Hatk if not h % Hatk else h//Hatk+1
      #사람이 먼저 때리므로 (turn -1) * 공격력 만큼의 피해를 입는다
      Hcur -= a * (turn-1)

    if Hcur <= 0:
        return False
  return True

high = N*1000000*1000000
low = 1

while high >= low :
  mid = (high + low) //2 
  if canClear(mid, atk) :
    high = mid -1
    answer = mid
  else :
    low = mid + 1

print(answer)