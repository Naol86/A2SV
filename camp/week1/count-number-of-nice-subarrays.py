class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        _dict = defaultdict(int)
        num = 0
        preFix = 0
        _dict[0] = 1
        for i in nums:
            if i % 2 != 0:
                preFix += 1
            num += _dict[preFix - k]
            _dict[preFix] += 1
        return num