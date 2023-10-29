n, k = map(int, input().split())

print("n:", n, "k:",k)

count = 0

while n > 1:
    # print("while문 진입 ==========>")
    if n % k != 0:
        # print("if 진입")
        n -= 1
        count += 1
    elif n % k == 0:
        # print("elif 진입")
        n /= k
        count += 1
        
print(count)