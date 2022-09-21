from collections import deque
import sys

sys.stdin = open("1158_요세푸스문제_input.txt", "r")
n, k = map(int, sys.stdin.readline().split(" "))
queue = deque([i for i in range(1, n+1)])
result = []

while queue:
    queue.rotate(-(k-1))
    result.append(queue.popleft())

print("<", ", ".join(map(str, result)), ">", sep="")
