from collections import deque


def solution(maps):
    n = len(maps)
    m = len(maps[0])
    dx = [-1, 0, 1, 0]
    dy = [0, 1, 0, -1]
    dq = deque()
    distance = [[0] * m for _ in range(n)]
    check = [[0] * m for _ in range(n)]
    distance[0][0] = 1
    check[0][0] = 1
    dq.append((0, 0))

    while dq:
        tmp = dq.popleft()

        for i in range(4):
            x = tmp[0] + dx[i]
            y = tmp[1] + dy[i]

            if (0 <= x < n) and (0 <= y < m) and (maps[x][y] == 1) and (check[x][y] == 0):
                check[x][y] = 1
                distance[x][y] = distance[tmp[0]][tmp[1]] + 1
                dq.append((x, y))

    if distance[n - 1][m - 1]:
        return distance[n - 1][m - 1]
    else:
        return -1


print(solution([[1, 0, 1, 1, 1, 0], [1, 0, 1, 0, 1, 0], [1, 0, 1, 1, 1, 0], [1, 1, 1, 0, 1, 1], [0, 0, 0, 0, 1, 1]]))
