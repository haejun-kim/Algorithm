import sys
sys.stdin = open("2775_부녀회장이될테야_input.txt", "rt")

t = int(sys.stdin.readline())

for _ in range(t):
    k = int(sys.stdin.readline())
    n = int(sys.stdin.readline())
    floor_0 = [i for i in range(1, n + 1)]  # 0층 n 호수까지 인원 채우기

    for i in range(k):
        for j in range(1, n):
            floor_0[j] += floor_0[j - 1]

    print(floor_0[-1])
