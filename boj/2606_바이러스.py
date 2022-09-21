import sys

sys.stdin = open("2606_바이러스_input.txt", "r")
computers = int(sys.stdin.readline().strip())
lines = int(sys.stdin.readline().strip())
graph = [[] * computers for _ in range(computers + 1)]
check = [0] * (computers + 1)
cnt = 0

for _ in range(lines):
    a, b = map(int, sys.stdin.readline().split())
    graph[a].append(b)
    graph[b].append(a)


def dfs(start):
    global cnt
    check[start] = 1

    for computer in graph[start]:
        if check[computer] == 0:
            dfs(computer)
            cnt += 1


dfs(1)
print(cnt)
