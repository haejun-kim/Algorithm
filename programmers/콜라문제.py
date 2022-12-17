def solution(a, b, n):
    cnt = 0

    while n >= a:
        d, m = divmod(n, a)
        n = d * b + m
        cnt += d * b

    return cnt


print(solution(3, 1, 20))
