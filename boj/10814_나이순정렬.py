import sys
sys.stdin = open("10814_나이순정렬_input.txt", "rt")

n = int(sys.stdin.readline())
people = [sys.stdin.readline().rstrip().split() for _ in range(n)]

people.sort(key=lambda x: int(x[0]))

for person in people:
    print(person[0], person[1])
