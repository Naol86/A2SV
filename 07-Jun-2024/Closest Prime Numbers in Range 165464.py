# Problem: Closest Prime Numbers in Range - https://leetcode.com/problems/closest-prime-numbers-in-range/

class Solution:
    def closestPrimes(self, left: int, right: int) -> List[int]:
        seiv = [True] * (right + 1)
        seiv[0] = False
        seiv[1] = False
        for i in range(2, right + 1):
            if not seiv[i]:
                continue
            j = i * 2
            while j < right + 1:
                seiv[j] = False
                j += i
        _min = float('inf')
        ans = [-1, -1]
        pre = None
        for i in range(left, right + 1):
            if seiv[i]:
                if not pre:
                    pre = i
                elif i - pre < _min:
                    ans = [pre, i]
                    _min = i - pre
                pre = i
        # print(seiv)
        return ans