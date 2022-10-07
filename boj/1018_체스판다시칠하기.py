import sys
sys.stdin = open("1018_체스판다시칠하기_input.txt", "rt")

n, m = map(int, sys.stdin.readline().split())
board = [sys.stdin.readline().rstrip() for _ in range(n)]
start_with_white = "WBWBWBWB"
start_with_black = "BWBWBWBW"
check_white = [
    start_with_white, start_with_black,
    start_with_white, start_with_black,
    start_with_white, start_with_black,
    start_with_white, start_with_black
]
check_black = [
    start_with_black, start_with_white,
    start_with_black, start_with_white,
    start_with_black, start_with_white,
    start_with_black, start_with_white,
]
board_size = 8
result = float("inf")


def solve(x, y):
    count_white = 0
    count_black = 0

    for dx in range(board_size):
        for dy in range(board_size):
            nx = x + dx
            ny = y + dy

            if board[nx][ny] != check_white[dx][dy]:
                count_white += 1
            if board[nx][ny] != check_black[dx][dy]:
                count_black += 1

    return min(count_white, count_black)


for i in range(n - board_size + 1):
    for j in range(m - board_size + 1):
        result = min(result, solve(i, j))

print(result)
