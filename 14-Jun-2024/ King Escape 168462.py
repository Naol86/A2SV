# Problem:  King Escape - https://codeforces.com/problemset/problem/1033/A

x = int(input())
ax, ay = map(int, input().split())
bx, by = map(int, input().split())
cx, cy = map(int, input().split())

bx -= ax
cx -= ax
by -= ay
cy -= ay
if ((bx < 0 )== (cx < 0)) and ((by < 0) == (cy < 0)):
  print("YES")
else:
  print("NO")