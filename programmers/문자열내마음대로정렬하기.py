def solution(strings, n):
    index_string_dict = {}

    for string in strings:
        index_string_dict[string] = string[n:n+1]

    index_string_dict = sorted(index_string_dict.items(), key=lambda item: (item[1], item[0]))

    return [index_string_dict[i][0] for i in range(len(index_string_dict))]


print(solution(["abce", "abcd", "cdx"], 2))
