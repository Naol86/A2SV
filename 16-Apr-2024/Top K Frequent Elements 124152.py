# Problem: Top K Frequent Elements - https://leetcode.com/problems/top-k-frequent-elements/

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = Counter(nums)
        lis = []
        for key, value in count.items():
            lis.append((-value, key))
        
        heapq.heapify(lis)
        ans = []
        while k > 0:
            temp = heapq.heappop(lis)
            ans.append(temp[1])
            k -= 1
        return ans
