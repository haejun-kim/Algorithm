import sys
sys.stdin = open("9461_파도반수열_input.txt", "rt")

t = int(sys.stdin.readline())

for i in range(t):
    n = int(sys.stdin.readline())
    dp = [0] * 101
    dp[1], dp[2], dp[3] = 1, 1, 1

    for j in range(1, n - 2):
        dp[j + 3] = dp[j] + dp[j + 1]

    print(dp[n])
