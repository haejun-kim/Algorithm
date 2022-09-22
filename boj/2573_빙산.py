from collections import deque
import sys

sys.stdin = open("2573_빙산_input.txt", "r")
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
n, m = map(int, sys.stdin.readline().split())
iceberg = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
queue = deque()
check = False


def bfs(x, y):
    queue.append((x, y))

    while queue:
        x, y = queue.popleft()
        visit_check[x][y] = 1

        for k in range(4):
            nx = x + dx[k]
            ny = y + dy[k]

            if 0 <= nx < n and 0 <= ny < m:
                if iceberg[nx][ny] and not visit_check[nx][ny]:
                    visit_check[nx][ny] = 1
                    queue.append((nx, ny))
                elif not iceberg[nx][ny]:
                    zero_count[x][y] += 1

    return 1  # 한번 순회했다는 카운팅


while True:
    visit_check = [[0] * m for _ in range(n)]
    zero_count = [[0] * m for _ in range(n)]
    result = []
    for i in range(n):
        for j in range(m):
            if iceberg[i][j] and not visit_check[i][j]:
                result.append(bfs(i, j))

    for i in range(n):
        for j in range(m):
            iceberg[i][j] -= zero_count[i][j]
            if iceberg[i][j] < 0:
                iceberg[i][j] = 0

    if len(result) == 0:
        break
    if len(result) >= 2:
        check = True
        break

if check:
    print(len(result))
else:
    print(0)

