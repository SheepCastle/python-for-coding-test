n = int(input())
plans = map(str, input().split())

x, y = 1, 1

for plan in plans:
  if plan == "L":
    x -= 1
    if x < 1:
      x = 1
  elif plan == "R":
    x += 1
    if x > n:
      x = n
  elif plan == "U":
    y -= 1
    if y < 1:
      y = 1
  elif plan == "D":
    y += 1
    if y > n:
      y = n
  print(y, x)

print("좌표값은", y, x)