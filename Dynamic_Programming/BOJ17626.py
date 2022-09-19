# Four Squares

# 런타임 에러 (RecursionError)
# import sys
# sys.setrecursionlimit(10000)
#
# input = sys.stdin.readline
#
# n = int(input().strip())
#
# dp = [-1 for _ in range(n + 1)]
#
#
# def func(num):
#     if dp[num] != -1:
#         return dp[num]
#
#     if num == 0 or num == 1:
#         dp[num] = num
#
#     else:
#         minValue = 50001
#         i = 1
#         while i * i <= num:
#             minValue = min(minValue, func(num - i * i))
#             i += 1
#         dp[num] = minValue + 1
#
#     return dp[num]
#
#
# print(func(n))

# ---

import sys
from math import sqrt

input = sys.stdin.readline

n = int(input().strip())
dp = [99999 for _ in range(50001)]

for i in range(1, n + 1):
    if int(sqrt(i)) * int(sqrt(i)) == i:
        dp[i] = 1

for i in range(1, n + 1):
    for j in range(1, int(sqrt(i))):
        dp[i] = min(dp[i], dp[j * j] + dp[i - j * j])

print(dp[n])
