def convert_binary(n, arr):
    return [bin(num)[2:].zfill(n) for num in arr]


def solution(n, arr1, arr2):
    arr1 = convert_binary(n, arr1)
    arr2 = convert_binary(n, arr2)

    array = [str(int(arr1[i]) + int(arr2[i])).zfill(n) for i in range(len(arr1))]

    result = []
    for x in array:
        tmp = ""
        for k in x:
            if k != "0":
                tmp += "#"
            else:
                tmp += " "

        result.append("".join(tmp))

    return result


print(solution(6, [46, 33, 33, 22, 31, 50], [27, 56, 19, 14, 14, 10]))
