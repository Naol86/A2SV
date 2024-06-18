# Problem: Can I Square? - https://codeforces.com/contest/1915/problem/C

import math


for _ in range(int(input())):
    x = int(input())
    lis = [int(i) for i in input().split()]
    
    _sum = sum(lis)
    x = int(math.sqrt(_sum))
    if math.pow(x, 2) == _sum:
        print("YES")
    else:
        print("NO")