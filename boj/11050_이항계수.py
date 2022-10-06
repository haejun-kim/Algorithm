from math import factorial
import sys
sys.stdin = open("11050_이항계수_input.txt", "rt")

n, k = map(int, sys.stdin.readline().split())
print(factorial(n) // (factorial(k) * factorial(n-k)))