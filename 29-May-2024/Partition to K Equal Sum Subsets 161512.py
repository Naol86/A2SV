# Problem: Partition to K Equal Sum Subsets - https://leetcode.com/problems/partition-to-k-equal-sum-subsets/

class Solution:
    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:
        # sum of nums
        _sum = sum(nums)

        # sum is has to be divisible with k
        if _sum % k:
            return False

        nums.sort(reverse=True)
        # capcity of one buk
        cap = _sum // k
        buk = [0] * k
        memo = set()
        used = 0
        def back_tracking(i):
            nonlocal cap, used
            if i >= len(nums):
                if used == (1<<(len(nums))) - 1:
                    return True
                return False
            for j in range(k):
                # if (i, buk[j]') in memo:
                #     continue'
                if buk[j] + nums[i] <= cap:
                    buk[j] += nums[i]
                    used ^= (1<<i)
                    memo.add((i, buk[j]))
                    if back_tracking(i + 1):
                        return True
                    buk[j] -= nums[i]
                    used ^= (1<<i)
                if buk[j] == 0:
                    break
            return False
        ans = back_tracking(0)
        # print(memo)
        return ans