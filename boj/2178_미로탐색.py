from collections import deque
import sys

sys.stdin = open("2178_미로탐색_input.txt", "r")
dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]
n, m = map(int, sys.stdin.readline().split())
board = [list(map(int, sys.stdin.readline().rstrip())) for _ in range(n)]
distance = [[0] * m for _ in range(n)]
queue = deque()

queue.append((0, 0))
distance[0][0] = 1

while queue:
    tmp = queue.popleft()

    for i in range(4):
        x = tmp[0] + dx[i]
        y = tmp[1] + dy[i]

        if (0 <= x < n) and (0 <= y < m) and (board[x][y] == 1) and (distance[x][y] == 0):
            distance[x][y] = distance[tmp[0]][tmp[1]] + 1
            queue.append((x, y))

print(distance[n-1][m-1])
