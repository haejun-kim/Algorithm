from collections import deque
import sys

sys.stdin = open("9205_맥주마시면서걸어가기_input.txt", "r")
t = int(sys.stdin.readline())


def bfs():
    queue = deque()
    queue.append((home[0], home[1]))

    while queue:
        x, y = queue.popleft()

        if abs(x - rock_festival[0]) + abs(y - rock_festival[1]) <= 1000:
            print("happy")
            return

        for i in range(n):
            if not visit_check[i]:
                nx, ny = convenience_store[i]

                if abs(x - nx) + abs(y - ny) <= 1000:
                    queue.append((nx, ny))
                    visit_check[i] = 1

    print("sad")
    return


for _ in range(t):
    n = int(sys.stdin.readline())  # 편의점 개수
    home = list(map(int, sys.stdin.readline().split()))
    convenience_store = [tuple(map(int, sys.stdin.readline().split())) for _ in range(n)]
    rock_festival = list(map(int, sys.stdin.readline().split()))
    visit_check = [0 for _ in range(n+1)]
    bfs()
