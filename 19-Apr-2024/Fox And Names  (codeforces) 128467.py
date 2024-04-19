# Problem: Fox And Names  (codeforces) - https://codeforces.com/contest/510/problem/C

from collections import defaultdict, deque


graph = defaultdict(list)
inDegree = [0] * 26
lis = []
ans = []
for _ in range(int(input())):
  lis.append(input())
def get_dependency(n):
  _min = min(len(lis[n]), len(lis[n+1]))
  for i in range(_min):
    if lis[n][i] != lis[n+1][i]:
      graph[lis[n][i]].append(lis[n+1][i])
      inDegree[ord(lis[n+1][i]) - ord('a')] += 1
      break
  else:
    if len(lis[n]) > len(lis[n+1]):
      print("Impossible")
      exit()

for i in range(len(lis) - 1):
  get_dependency(i)


visited = [0] * 26
for i in range(26):
  if inDegree[i] != 0 or visited[i] != 0:
    continue
  stack = deque([chr(ord('a') + i)])
  # ans.append(chr(ord('a') + i))
  while stack:
    x = stack.popleft()
    visited[ord(x) - ord('a')] += 1
    ans.append(x)
    for node in graph[x]:
      inDegree[ord(node) - ord('a')] -= 1
      if inDegree[ord(node) - ord('a')] == 0:
        stack.append(node)
        # ans.append(node)
if len(ans) != 26:
  print('Impossible')
else:
  print(''.join(ans))
# print(inDegree)
# print(ans, len(ans))
