#직사각형 판별식

while(1):
  num = list(map(int, input().split()))
  if sum(num) == 0:
    break
  num.sort() # 오름차순 정리

  if (num[2] ** 2) == (num[0] ** 2) + (num[1] ** 2): # or pow()
    print("right")
  else:
    print("wrong")
