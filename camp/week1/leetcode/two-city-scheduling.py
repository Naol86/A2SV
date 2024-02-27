class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        temp = []
        for i in range(len(costs)):
            temp.append((costs[i][0] - costs[i][1], i))
        temp.sort()
        ans = 0
        for i in range(len(costs)):
            if i < len(costs)//2:
                ans += costs[temp[i][1]][0]
            else:
                ans += costs[temp[i][1]][1]
        return ans