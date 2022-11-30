N = int(input())
AList = list(map(int, input().split()))
M = int(input())
MList = list(map(int, input().split()))

AList.sort()

def binarySearch(num) :
  low = 0
  high = N-1
  while(low <= high) :
    mid = (low + high) //2 
    if AList[mid] == num :
      return 1
    if AList[mid] > num  :
      high = mid -1
    else : 
      low = mid + 1
  return 0
for i in MList :
  print(binarySearch(i))