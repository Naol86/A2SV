# Problem: Most Profit Assigning Work - https://leetcode.com/problems/most-profit-assigning-work/

class Solution:
    def maxProfitAssignment(self, difficulty: List[int], profit: List[int], worker: List[int]) -> int:
        new_array = [(difficulty[i], profit[i]) for i in range(len(profit))]
        new_array.sort()
        worker.sort()

        ans = 0
        _max = 0
        k = 0

        for i in range(len(worker)):
            while k < len(difficulty) and new_array[k][0] <= worker[i]:
                _max = max(_max, new_array[k][1])
                k += 1
            ans += _max
        
        return ans

