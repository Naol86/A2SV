# Problem: Way Too Long Words - https://codeforces.com/problemset/problem/71/A

for _ in range(int(input())):
  s = input()
  if len(s) < 11:
    print(s)
  else:
    print(f"{s[0]}{len(s) - 2}{s[-1]}")