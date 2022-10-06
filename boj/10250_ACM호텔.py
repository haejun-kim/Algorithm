import sys
sys.stdin = open("10250_ACM호텔_input.txt", "rt")

t = int(sys.stdin.readline())

for _ in range(t):
    h, w, n = list(map(int, sys.stdin.readline().split()))
    room = (n // h) + 1
    floor = n % h
    if n % h == 0:
        room = n // h
        floor = h

    print(f"{floor}{str(room).zfill(2)}")
