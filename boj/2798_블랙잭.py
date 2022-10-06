from itertools import combinations
import sys
sys.stdin = open("2798_블랙잭_input.txt", "rt")

n, m = map(int, sys.stdin.readline().rstrip().split())
max = float("-inf")
cards = list(map(int, sys.stdin.readline().rstrip().split()))
cards = list(combinations(cards, 3))

for card in cards:
    if sum(card) >= max:
        if sum(card) <= m:
            max = sum(card)

print(max)
