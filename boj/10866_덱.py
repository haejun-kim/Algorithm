from collections import deque
import sys

sys.stdin = open("10866_덱_input.txt", "r")
n = int(sys.stdin.readline())
queue = deque()

for _ in range(n):
    cmd = sys.stdin.readline().rstrip()

    if "push" in cmd:
        command, x = cmd.split(" ")
        if command == "push_back":
            queue.append(x)
        elif command == "push_front":
            queue.appendleft(x)
    if cmd == "pop_front":
        if queue:
            print(queue.popleft())
        else:
            print(-1)
    if cmd == "pop_back":
        if queue:
            print(queue.pop())
        else:
            print(-1)
    if cmd == "size":
        print(len(queue))
    if cmd == "empty":
        if queue:
            print(0)
        else:
            print(1)
    if cmd == "front":
        if queue:
            print(queue[0])
        else:
            print(-1)
    if cmd == "back":
        if queue:
            print(queue[-1])
        else:
            print(-1)
