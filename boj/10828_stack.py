import sys
sys.stdin = open("10828_stack_input.txt", "r")
n = int(sys.stdin.readline())
stack = list()

for _ in range(n):
    command = sys.stdin.readline().rstrip()
    if "push" in command:
        _, num = command.split(" ")
        stack.append(num)
    elif command == "top":
        if stack:
            print(stack[-1])
        else:
            print(-1)
    elif command == "size":
        print(len(stack))
    elif command == "empty":
        if stack:
            print(0)
        else:
            print(1)
    elif command == "pop":
        if stack:
            print(stack.pop())
        else:
            print(-1)
