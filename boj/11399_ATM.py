import sys

sys.stdin = open("11399_ATM_input.txt", "r")
n = int(sys.stdin.readline())
waits = list(map(int, sys.stdin.readline().split()))
times = 0
result = []

waits.sort()

for i in waits:
    times = i + times
    result.append(times)

print(sum(result))
