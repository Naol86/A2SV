# Problem: New Year Transportation - https://codeforces.com/problemset/problem/500/A

# using map
# m, t = map(int, input().split())
m, t = [int(i) for i in input().split()]

nums = [int(i) for i in input().split()]

i = 1
while i < t:
  i += nums[i-1]
  if i == t:
    print("YES")
    break
else:
  print("NO")
