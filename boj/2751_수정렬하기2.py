import sys
sys.stdin = open("2751_수정렬하기2_input.txt", "rt")

n = int(sys.stdin.readline())
nums = [int(sys.stdin.readline()) for _ in range(n)]
nums.sort()

for i in nums:
    print(i)
