import sys
sys.stdin = open("1920_수찾기_input.txt", "rt")

n = int(sys.stdin.readline())
n_list = set(map(int, sys.stdin.readline().split()))
m = int(sys.stdin.readline())
m_list = list(map(int, sys.stdin.readline().split()))

for m in m_list:
    if m in n_list:
        print(1)
    else:
        print(0)
