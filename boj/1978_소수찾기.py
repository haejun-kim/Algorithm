import sys

sys.stdin = open("1978_소수찾기_input.txt", "r")
n = int(sys.stdin.readline())
nums = list(map(int, sys.stdin.readline().split()))
result = 0

for num in nums:
    cnt = 0  # 숫자마다 카운팅을 해야하기 때문에 초기화
    if num > 1:
        for i in range(2, num+1):
            if num % i == 0:  # 소수가 아님
                cnt += 1
        if cnt == 1:  # 1을 제외하고 약수가 본인밖에 없다는 의미. 따라서 소수로 판단.
            result += 1

print(result)
