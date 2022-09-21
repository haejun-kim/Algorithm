from collections import deque
import sys

sys.stdin = open("1260_DFS_BFS_input.txt", "r")
n, m, v = map(int, sys.stdin.readline().split())
graph = [[0] * (n+1) for _ in range(n+1)]
dfs_check = [0] * (n+1)
bfs_check = [0] * (n+1)


def dfs(start):
    dfs_check[start] = 1
    print(start, end=" ")
    for i in range(1, n+1):
        if graph[start][i] == 1 and dfs_check[i] == 0:
            dfs_check[i] = 1
            dfs(i)


def bfs(start):
    queue = deque()
    queue.append(start)
    bfs_check[start] = 1

    while queue:
        res = queue.popleft()
        print(res, end=" ")
        for i in range(1, n+1):
            if graph[res][i] == 1 and bfs_check[i] == 0:
                queue.append(i)
                bfs_check[i] = 1


for _ in range(m):
    x, y = map(int, sys.stdin.readline().split())
    graph[x][y] = graph[y][x] = 1

dfs(v)
print()
bfs(v)
