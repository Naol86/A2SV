class Solution:
    def getCommon(self, nums1: List[int], nums2: List[int]) -> int:
        upper = 0
        lower = 0
        leng_1 = len(nums1)
        leng_2 = len(nums2)
        while upper < leng_1 and lower < leng_2:
            if nums1[upper] == nums2[lower]:
                return nums1[upper]
            elif nums1[upper] > nums2[lower]:
                lower += 1
            else:
                upper += 1
        return -1