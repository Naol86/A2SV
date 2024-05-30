# Problem: Minimum XOR Sum of Two Arrays - https://leetcode.com/problems/minimum-xor-sum-of-two-arrays/

class Solution:
    def minimumXORSum(self, nums1: List[int], nums2: List[int]) -> int:
        n = len(nums1)
        memo = {}
        
        def rec(indx1, used):
            if (indx1, used) not in memo:
                if indx1 == n:
                    return 0
                temp = float('inf')
                for i in range(n):
                    if not (used & (1<<i)):
                        used ^= (1<<i)
                        temp = min(temp, (nums1[indx1] ^ nums2[i]) + rec(indx1 + 1, used))
                        used ^= (1<<i)
                memo[(indx1, used)] = temp
            return memo[(indx1, used)]
        
        ans = rec(0, 0)
        # print(memo)
        return ans