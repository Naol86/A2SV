# Problem: Segment with Small Sum - https://codeforces.com/edu/course/2/lesson/9/2/practice/contest/307093/problem/A

a, n = map(int, input().split())
nums = [int(i) for i in input().split()]

left = right = 0
_sum = 0
_max = 0
while right < a:
  while _sum + nums[right] > n:
    _sum -= nums[left]
    left += 1
  _sum += nums[right]
  right += 1
  _max = max(_max, right - left)
print(_max)