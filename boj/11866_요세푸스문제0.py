from collections import deque
import sys
sys.stdin = open("11866_요세푸스문제0_input.txt")

n, k = list(map(int, sys.stdin.readline().split()))
deque = deque([i for i in range(1, n + 1)])
ret = []

for _ in range(n):
    deque.rotate(-(k - 1))
    ret.append(deque.popleft())

print(f"<{', '.join(map(str, ret))}>")
