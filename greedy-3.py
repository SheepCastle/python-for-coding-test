# N, M, K를 공백으로 구분하여 입력 받기
n, m, k = map(int, input().split())
# N개의 수를 공백으로 구분하여 입력받기
data = list(map(int, input().split()))

data.sort() # 입력 받은 수들 정렬하기
first = data[n-1] # 제일 큰 수
second = data[n-2] # 두번째로 큰 수

result = 0

while True:
    for i in range(k): # 가장 큰 수를 K 번 더하기
        if m == 0:
            break
        result += first
        m -= 1
    if m == 0:
        break
    result += second
    m -= 1

print(result)