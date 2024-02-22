class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        hash_map = {}
        stack = []
        for i in nums2:
            hash_map[i] = -1
            while stack and stack[-1] < i:
                hash_map[stack.pop()] = i
            stack.append(i)
        ans = []
        for i in nums1:
            ans.append(hash_map[i])
        return ans