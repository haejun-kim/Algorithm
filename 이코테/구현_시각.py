import sys

n = int(sys.stdin.readline())
minutes, seconds = 60, 60
cnt = 0

for time in range(n+1):
    for minute in range(minutes):
        for second in range(seconds):
            times = f"{time}:{minute}:{second}"

            if "3" in times:
                cnt += 1

print(cnt)
