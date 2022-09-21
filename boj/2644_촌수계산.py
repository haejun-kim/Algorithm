import sys
sys.setrecursionlimit(10**6)

sys.stdin = open("2644_촌수계산_input.txt", "r")
people = int(sys.stdin.readline().rstrip())
person1, person2 = map(int, sys.stdin.readline().split(" "))
m = int(sys.stdin.readline().rstrip())
graph = [[] for _ in range(people + 1)]
check = [0] * (people + 1)

for _ in range(m):
    a, b = map(int, sys.stdin.readline().split(" "))
    graph[a].append(b)
    graph[b].append(a)


def dfs(start):
    for i in graph[start]:
        if check[i] == 0:
            check[i] = check[start] + 1
            dfs(i)


dfs(person1)
print(check[person2] if check[person2] > 0 else -1)
