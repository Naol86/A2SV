# Problem: Minimal string - https://codeforces.com/contest/797/problem/C

s = input().strip()

t = []
u = []

# Frequency dictionary to keep track of remaining characters in s
from collections import Counter
remaining = Counter(s)

for char in s:
    # Add the current character to t
    t.append(char)
    remaining[char] -= 1
    if remaining[char] == 0:
        del remaining[char]
    
    # Check if we can pop from t to u
    while t and (not remaining or min(remaining) >= t[-1]):
        u.append(t.pop())

# Join u to form the resulting string
print(''.join(u))
