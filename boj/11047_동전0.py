import sys

sys.stdin = open("11047_동전0_input.txt", "r")
n, k = list(map(int, sys.stdin.readline().split()))
coins = [int(sys.stdin.readline().rstrip()) for _ in range(n)]
cnt = 0
coins.reverse()

for coin in coins:
    while coin <= k:
        k -= coin
        cnt += 1

print(cnt)
