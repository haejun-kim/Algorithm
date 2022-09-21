"""
push X: 정수 X를 큐에 넣는 연산이다.
pop: 큐에서 가장 앞에 있는 정수를 빼고, 그 수를 출력한다. 만약 큐에 들어있는 정수가 없는 경우에는 -1을 출력한다.
size: 큐에 들어있는 정수의 개수를 출력한다.
empty: 큐가 비어있으면 1, 아니면 0을 출력한다.
front: 큐의 가장 앞에 있는 정수를 출력한다. 만약 큐에 들어있는 정수가 없는 경우에는 -1을 출력한다.
back: 큐의 가장 뒤에 있는 정수를 출력한다. 만약 큐에 들어있는 정수가 없는 경우에는 -1을 출력한다.
"""
from collections import deque
import sys

sys.stdin = open("10845_큐_input.txt", "r")
n = int(sys.stdin.readline())
queue = deque()

for _ in range(n):
    cmd = sys.stdin.readline().rstrip()

    if "push" in cmd:
        _, x = cmd.split(" ")
        queue.append(x)

    elif cmd == "pop":
        if queue:
            print(queue.popleft())
        else:
            print(-1)

    elif cmd == "size":
        print(len(queue))

    elif cmd == "empty":
        if queue:
            print(0)
        else:
            print(1)

    elif cmd == "front":
        if queue:
            print(queue[0])
        else:
            print(-1)

    elif cmd == "back":
        if queue:
            print(queue[-1])
        else:
            print(-1)

