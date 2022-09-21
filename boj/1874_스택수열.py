import sys
sys.stdin = open("1874_스택수열_input.txt", "r")
n = int(sys.stdin.readline())
stack = []
answer = []
cur = 1

for _ in range(n):
    num = int(sys.stdin.readline())

    while cur <= num:
        stack.append(cur)
        answer.append("+")
        cur += 1

    if stack[-1] == num:
        stack.pop()
        answer.append("-")
    else:
        print("NO")
        break
else:
    for i in answer:
        print(i)
