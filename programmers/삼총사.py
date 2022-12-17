from itertools import combinations


def solution(number):
    cnt = 0

    for num in combinations(number, 3):
        if sum(num) == 0:
            cnt += 1

    return cnt


print(solution([-2, 3, 0, 2, -5]))
