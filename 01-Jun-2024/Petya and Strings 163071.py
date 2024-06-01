# Problem: Petya and Strings - https://codeforces.com/problemset/problem/112/A

a = input().lower()
b = input().lower()
if a == b:
  print(0)
elif a > b:
  print(1)
else:
  print(-1)