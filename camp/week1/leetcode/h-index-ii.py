class Solution:
    def hIndex(self, citations: List[int]) -> int:
        leng = len(citations)
        # if leng == 1:
        #     return 1
        # for i in range(leng):
        #     if citations[i] >= (leng - i):
        #         return leng - i
        # return 0
        left = 0
        right = leng - 1
        ans = 0
        while left <= right:
            mid = left + (right - left) // 2
            if citations[mid] >= (leng - mid):
                ans = leng - mid
                right = mid - 1
            else:
                left = mid + 1
        
        return ans
        
