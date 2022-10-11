import sys
sys.stdin = open("2292_벌집_input.txt", "rt")

n = int(sys.stdin.readline())
house = 1
cnt = 1

while n > house:
    house += 6 * cnt
    cnt += 1

print(cnt)
