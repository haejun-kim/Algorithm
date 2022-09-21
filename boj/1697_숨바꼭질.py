from collections import deque
import sys

sys.stdin = open("1697_숨바꼭질_input.txt", "r")
n, k = map(int, sys.stdin.readline().split())
max = 100000
distance = [0] * (max+1)


def bfs():
    queue = deque()
    queue.append(n)

    while queue:
        tmp = queue.popleft()
        if tmp == k:
            print(distance[tmp])
            break
        else:
            for i in (tmp-1, tmp+1, 2*tmp):
                if (0 <= i <= max) and (distance[i] == 0):
                    distance[i] = distance[tmp] + 1
                    queue.append(i)


bfs()
