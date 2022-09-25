import sys
sys.stdin = open("DP_개미전사_input.txt", "rt")

n = int(sys.stdin.readline())  # 3 <= n <= 100
array = list(map(int, sys.stdin.readline().split()))  # 0 <= k <= 1000
dp = [0] * 100

dp[0] = 0
dp[1] = max(array[0], array[1])
for i in range(2, n):
    dp[i] = max(dp[i - 1], dp[i - 2] + array[i])

print(dp[n-1])
