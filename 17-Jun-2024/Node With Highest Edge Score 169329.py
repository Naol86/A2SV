# Problem: Node With Highest Edge Score - https://leetcode.com/problems/node-with-highest-edge-score/description/

class Solution:
    def edgeScore(self, edges: List[int]) -> int:
        ans = 0
        _max = 0
        nums = [0] * len(edges)
        for i in range(len(edges)):
            nums[edges[i]] += i
            if _max < nums[edges[i]]:
                _max = nums[edges[i]]
                ans = edges[i]
            elif _max == nums[edges[i]] and edges[i] < ans:
                ans = edges[i]
            
        return ans