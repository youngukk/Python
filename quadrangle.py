# 4번째 점

x_ = []
y_ = []

# 좌표 입력
for i in range(3):
  x, y = map(int, input().split())
  x_.append(x)
  y_.append(y)

# 좌표 판별
for i in range(3):
  if x_.count(x_[i]) == 1:
    x = x_[i]
  if y_.count(y_[i]) == 1:
    y = y_[i]

print(x, y)