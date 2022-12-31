def solution(clothes):
    clothes_dict = {}
    cnt = 1

    for cloth in clothes:
        if cloth[1] in clothes_dict:
            clothes_dict[cloth[1]].append(cloth[0])
        else:
            clothes_dict[cloth[1]] = [cloth[0]]

    for key in clothes_dict.keys():
        cnt *= (len(clothes_dict[key]) + 1)

    return cnt - 1


print(solution(
    [
        ["yellow_hat", "headgear"],
        ["blue_sunglasses", "eyewear"],
        ["green_turban", "headgear"]
    ]
))
