class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        dp = []
        for i in nums:
            index = bisect_left(dp, i)
            print(index)
            if index < len(dp):
                dp[index] = i
            else:
                dp.append(i)
            print(dp)
        if len(dp) >= 3:
            return True
        return False
        