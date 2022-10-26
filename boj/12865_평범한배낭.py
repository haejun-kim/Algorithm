import sys
sys.stdin = open("12865_평범한배낭_input.txt", "rt")

n, k = map(int, sys.stdin.readline().split())
dp = [0] * (k + 1)

for i in range(n):
    weight, value = map(int, sys.stdin.readline().split())
    for j in range(weight, k + 1):
        dp[j] = max(dp[j], dp[j - weight] + value)

print(max(dp))
