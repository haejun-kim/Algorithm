"""
L	커서를 왼쪽으로 한 칸 옮김 (커서가 문장의 맨 앞이면 무시됨)
D	커서를 오른쪽으로 한 칸 옮김 (커서가 문장의 맨 뒤이면 무시됨)
B	커서 왼쪽에 있는 문자를 삭제함 (커서가 문장의 맨 앞이면 무시됨)
    삭제로 인해 커서는 한 칸 왼쪽으로 이동한 것처럼 나타나지만, 실제로 커서의 오른쪽에 있던 문자는 그대로임
P $	$라는 문자를 커서 왼쪽에 추가함
"""
# 시간 통과 풀이
import sys
sys.stdin = open("1406_에디터_input.txt", "r")
strings = [string for string in sys.stdin.readline().rstrip()]
cursor = []
n = int(sys.stdin.readline())

for _ in range(n):
    cmd = sys.stdin.readline().rstrip()

    if cmd == "L" and strings:
        cursor.append(strings.pop())

    elif cmd == "D" and cursor:
        strings.append(cursor.pop())

    elif cmd == "B" and strings:
        strings.pop()

    elif "P" in cmd:
        _, obj = cmd.split(" ")
        strings.append(obj)

cursor.reverse()
print("".join(strings + cursor))

# 시간 초과 풀이
# strings.append("cursor")
# n = int(sys.stdin.readline())
#
# for _ in range(n):
#     cmd = input()
#     idx = strings.index("cursor")
#
#     if "P" in cmd:
#         _, obj = cmd.split(" ")
#         strings.insert(idx, obj)
#
#     elif cmd == "L":
#         if strings[0] != "cursor":
#             cursor = strings.pop(idx)
#             strings.insert(idx-1, cursor)
#
#     elif cmd == "D":
#         if strings[-1] != "cursor":
#             cursor = strings.pop(idx)
#             strings.insert(idx+1, cursor)
#
#     elif cmd == "B":
#         if strings[0] != "cursor":
#             strings.pop(idx-1)
#
# strings.pop(strings.index("cursor"))
# print("".join(strings))
