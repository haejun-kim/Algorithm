import sys
sys.stdin = open("DP_효율적인화폐구성_input.txt", "rt")

n, m = list(map(int, sys.stdin.readline().split()))
array = [map(int, sys.stdin.readline()) for _ in range(n)]
dp = [10001] * (m + 1)

dp[0] = 0

