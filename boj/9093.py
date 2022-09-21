import sys
sys.stdin = open("9093_input.txt", "r")
n = int(sys.stdin.readline())

for _ in range(n):
    strings = [string[::-1] for string in input().split(" ")]
    print(" ".join(strings))
