# Problem: Kth Largest Element in a Stream - https://leetcode.com/problems/kth-largest-element-in-a-stream/

class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.nums = []
        self.k = k
        for i in range(k):
            if i < len(nums):
                heapq.heappush(self.nums, nums[i])
        i = k
        while i < len(nums):
            if self.nums[0] < nums[i]:
                heapq.heapreplace(self.nums, nums[i])
            i += 1

    def add(self, val: int) -> int:
        if len(self.nums) < self.k:
            heapq.heappush(self.nums, val)
            return self.nums[0]
        if self.nums and self.nums[0] < val:
            heapq.heapreplace(self.nums, val)
        if self.nums:
            return self.nums[0]
        return 0
        


        


# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)