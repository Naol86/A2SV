# Problem: Team - https://codeforces.com/contest/231/problem/A

ans = 0
for _ in range(int(input())):
  nums = [int(i) for i in input().split()]
  if sum(nums) > 1:
    ans +=1 
print(ans)