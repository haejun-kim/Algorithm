import math
import sys
sys.stdin = open("2609_최대공약수와최소공배수_input.txt", "rt")

x, y = map(int, sys.stdin.readline().split())
print(math.gcd(x, y))
print(math.lcm(x, y))
