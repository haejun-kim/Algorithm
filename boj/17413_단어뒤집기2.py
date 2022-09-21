from collections import deque
import sys

sys.stdin = open("17413_단어뒤집기2_input.txt", "r")
strings = sys.stdin.readline()
stack = []
queue = deque()

for k, v in enumerate(strings):
    if v == "<":
        while True:
            queue.append(v)
            if v == ">":
                break
    print(queue)