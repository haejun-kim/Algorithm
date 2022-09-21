import sys
sys.stdin = open("9012_input.txt", "r")
n = int(sys.stdin.readline())

for _ in range(n):
    stack = list()
    parenthesis_string = input()

    for ps in parenthesis_string:
        if ps == "(":
            stack.append(ps)
        elif ps == ")":
            if stack:
                stack.pop()
            else:
                print("NO")
                break
    else:
        if stack:
            print("NO")
        else:
            print("YES")
