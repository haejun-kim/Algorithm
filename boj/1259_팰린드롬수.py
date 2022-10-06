import sys
sys.stdin = open("1259_팰린드롬수_input.txt", "rt")

while True:
    test_case = sys.stdin.readline().rstrip()
    if test_case == "0":
        break
    if test_case == test_case[::-1]:
        print("yes")
    else:
        print("no")
