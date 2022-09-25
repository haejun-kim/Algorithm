from collections import Counter
import sys

sys.stdin = open("10816_숫자카드2_input.txt", "r")
n = int(sys.stdin.readline())
n_list = list(map(int, sys.stdin.readline().split()))
n_counter = Counter(n_list)
m = int(sys.stdin.readline())
m_list = list(map(int, sys.stdin.readline().split()))

print(' '.join(str(n_counter[m]) if m in n_counter else '0' for m in m_list))
