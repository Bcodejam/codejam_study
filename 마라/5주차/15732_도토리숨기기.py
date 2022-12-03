N, K , D = map(int, input().split())
lst = []


for _ in range(K) :
  lst.append(list(map(int, input().split())))

  
#maxend 번째 상자까지 도토리가 몇개 들어갈수있는지
def countD(maxEnd) :
  sum = 0
  for start, end, length in lst :
    #규칙이 기준상자 뒤에 있을경우 계산 X
    if maxEnd < start :
      continue
    realEnd = min(end, maxEnd)
    sum += ((realEnd-start)//length + 1)
  return sum



def binary() :
  answer = 0
  low = 0
  high = N
  #이분탐색으로 mid 번째 상자까지 최대로 들어갈수있는 도토리 수를 검사한다.
  while low <= high :
    mid = (low + high) //2 
    if countD(mid) < D :
      low = mid + 1
    if countD(mid) >= D:
      high = mid - 1
  return low

print(binary())