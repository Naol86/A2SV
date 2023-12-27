from collections import Counter
class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        num_1 = Counter(nums1)
        num_2 = Counter(nums2)
        ans = []
        for value in num_1:
            if value in num_2:
                ans += [value] * min(num_1[value], num_2[value])
        return ans