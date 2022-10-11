import sys
sys.stdin = open("2655_가장높은탑쌓기_input.txt", "rt")
n = int(sys.stdin.readline())
bricks = [(0, 0, 0, 0)]
for i in range(n):
    area, height, weight = map(int, sys.stdin.readline().split())
    bricks.append((i + 1, area, height, weight))
dp = [0] * (n + 1)
dp[0] = bricks[0][1]
max_height = bricks[0][1]

bricks.sort(reverse=True)

for i in range(1, n + 1):
    height = 0
    for j in range(i - 1, 0, -1):
        if bricks[j][2] > bricks[i][2] and dp[j] > height:
            height = dp[j]
    dp[i] = height + bricks[i][1]
    max_height = max(max_height, dp[i])

idx = n - 1
result = []

while idx > -1:
    if dp[idx] == max_height:
        result.append(bricks.index(bricks[idx]) + 1)
        max_height -= bricks[idx][1]
    idx -= 1

print(len(result))
print("\n".join(map(str, result)))
