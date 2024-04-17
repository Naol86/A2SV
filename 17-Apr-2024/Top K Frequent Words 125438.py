# Problem: Top K Frequent Words - https://leetcode.com/problems/top-k-frequent-words/

class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        count = Counter(words)
        heap = []
        for key, val in count.items():
            heapq.heappush(heap, (-val, key))
        ans = []
        temp = []
        pre = 0
        while k > 0 and heap:
            val, key = heapq.heappop(heap)
            if val != pre:
                temp.sort()
                ans.extend(temp)
                temp = []
                pre = val
            temp.append(key)
            k -= 1
        temp.sort()
        ans.extend(temp)
        return ans