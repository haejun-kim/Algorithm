from collections import deque


def solution(priorities, location):
    dq = deque([(i, v) for i, v in enumerate(priorities)])
    cnt = 0

    while True:
        if any(dq[0][1] < q[1] for q in dq):
            dq.rotate(-1)
        else:
            tmp = dq.popleft()
            cnt += 1

            if tmp[0] == location:
                return cnt


print(solution([1, 1, 9, 1, 1, 1], 0))
