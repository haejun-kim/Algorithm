def solution(s):
    x_cnt = 0
    not_x_cnt = 0
    result = 0
    x = s[:1]

    for idx, string in enumerate(s):
        if string == x:
            x_cnt += 1
        else:
            not_x_cnt += 1

        if x_cnt == not_x_cnt:
            x = s[idx+1:idx+2]
            result += 1
        else:
            try:
                s[idx+1]
            except IndexError:
                result += 1

    return result
