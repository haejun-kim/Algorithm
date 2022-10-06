import sys
sys.stdin = open("4153_직각삼각형_input.txt", "rt")

while True:
    test_case = list(map(int, sys.stdin.readline().rstrip().split()))
    test_case.sort()
    x, y, z = test_case[0], test_case[1], test_case[2]

    if x == 0 and y == 0 and z == 0:
        break

    if (x ** 2) + (y ** 2) == z ** 2:
        print("right")
    else:
        print("wrong")
