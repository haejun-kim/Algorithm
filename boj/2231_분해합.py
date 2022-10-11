import sys
sys.stdin = open("2231_분해합_input.txt", "rt")

n = int(sys.stdin.readline())


def solve(n):
    result = float("inf")

    for i in range(1, n + 1):
        num_list = []
        num_list.append(i)
        for num in str(i):
            num_list.append(int(num))

        if sum(num_list) == n:
            result = min(result, num_list[0])

            return result

    return 0


print(solve(n))
