from collections import deque


def solution(begin, target, words):
    if target not in words:
        return 0

    dq = deque()
    dq.append((begin, 0))

    while dq:
        tmp, cnt = dq.popleft()

        if tmp == target:
            return cnt

        for word in words:
            diff_cnt = 0

            for idx, v in enumerate(tmp):
                if v != word[idx]:
                    diff_cnt += 1

            if diff_cnt == 1:
                dq.append((word, cnt + 1))


print(solution("hit", "cog", ["hot", "dot", "dog", "lot", "log", "cog"]))
