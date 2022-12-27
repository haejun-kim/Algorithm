def dfs(com, computers, visited):
    visited[com] = True

    for idx, value in enumerate(computers[com]):
        if value and not visited[idx]:
            dfs(idx, computers, visited)


def solution(n, computers):
    visited = [False] * n
    cnt = 0

    for i in range(n):
        if not visited[i]:
            dfs(i, computers, visited)
            cnt += 1

    return cnt


print(solution(3, [[1, 1, 0], [1, 1, 0], [0, 0, 1]]))
