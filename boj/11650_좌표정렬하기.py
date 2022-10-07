import sys
sys.stdin = open("11650_좌표정렬하기_input.txt", "rt")

n = int(sys.stdin.readline())
nums = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
nums.sort(key=lambda x: (x[0], x[1]))

for num in nums:
    print(num[0], num[1])
