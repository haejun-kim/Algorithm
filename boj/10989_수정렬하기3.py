import sys
sys.stdin = open("10989_수정렬하기3_input.txt", "rt")

n = int(sys.stdin.readline())
nums = [int(sys.stdin.readline()) for _ in range(n)]
nums.sort()
print("\n".join(map(str, nums)))
