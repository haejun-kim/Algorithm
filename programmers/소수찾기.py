from itertools import permutations


def solution(numbers):
    nums = [x for n in numbers for x in n]
    result = []

    for i in range(1, len(nums) + 1):
        for x in set(permutations(nums, i)):
            x = int("".join(x))

            if x < 2:
                continue
            else:
                for j in range(2, int(x ** 0.5) + 1):
                    if x % j == 0:
                        break

                else:
                    result.append(x)
    return len(set(result))


print(solution("17"))
