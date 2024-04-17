# Problem: Find Median from Data Stream - https://leetcode.com/problems/find-median-from-data-stream/

class MedianFinder:

    def __init__(self):
        self.max_heap = []
        self.min_heap = []
        self.count = 0
        

    def addNum(self, num: int) -> None:
        if self.count % 2 == 0:
            heapq.heappush(self.max_heap, -num)
        else:
            heapq.heappush(self.min_heap, num)
        if self.min_heap and -self.max_heap[0] > self.min_heap[0]:
            x = heapq.heapreplace(self.max_heap, -self.min_heap[0])
            heapq.heapreplace(self.min_heap, - x)
        self.count += 1
        # print(self.max_heap, self.min_heap)

    def findMedian(self) -> float:
        if self.count % 2 != 0:
            return -self.max_heap[0]
        return (-self.max_heap[0] + self.min_heap[0]) / 2
        


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()