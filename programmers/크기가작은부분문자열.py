def solution(t, p):
    string_same_p_length = []
    p_length = len(p)
    cnt = 0

    for i in range(len(t) - (p_length - 1)):
        string_same_p_length.append(t[i:i + p_length])

    for string in string_same_p_length:
        if string <= p:
            cnt += 1

    return cnt


print(solution("500220839878", "7"))
