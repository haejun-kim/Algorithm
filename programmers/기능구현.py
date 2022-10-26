def solution(progresses, speeds):
    stack = []
    day = 0
    cnt = 0

    while len(progresses) > 0:
        if progresses[0] + (day * speeds[0]) >= 100:
            progresses.pop(0)
            speeds.pop(0)
            cnt += 1
        else:
            if cnt > 0:
                stack.append(cnt)
                cnt = 0
            day += 1

    stack.append(cnt)

    return stack


print(solution([93, 30, 55], [1, 30, 5]))
