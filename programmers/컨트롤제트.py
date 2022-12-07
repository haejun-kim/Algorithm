from collections import deque


def solution(s):
    dq = deque()
    strings = s.split(" ")

    for string in strings:
        if string != "Z":
            dq.append(string)
        else:
            dq.pop()

    return sum(map(int, dq))


print(solution("1 2 Z 3"))
