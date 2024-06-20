# Problem: A - abbccc - https://codeforces.com/gym/530187/problem/A

x = int(input())
s = input()

lis = []

i = 1
j = 0
while j < x:
  lis.append(s[j])
  j += i
  i += 1

print(''.join(lis))