from collections import deque
import sys
sys.stdin = open("2164_카드2_input.txt")

n = int(sys.stdin.readline())
deque = deque([i for i in range(1, n + 1)])

while len(deque) > 1:
    deque.popleft()
    deque.rotate(-1)

print(deque[0])
