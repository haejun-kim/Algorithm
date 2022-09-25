import sys
sys.stdin = open("1463_1로만들기_input.txt", "rt")

n = int(sys.stdin.readline())
dp = [0] * 1000001

for i in range(2, n + 1):
    dp[i] = dp[i - 1] + 1

    if i % 2 == 0:
        dp[i] = min(dp[i], dp[i // 2] + 1)

    if i % 3 == 0:
        dp[i] = min(dp[i], dp[i // 3] + 1)


print(dp[n])
