class Solution:
    def timeRequiredToBuy(self, tickets: List[int], k: int) -> int:
        if tickets[k] < 2:
            return k + tickets[k]
        ans = 0
        # left side
        for i in range(k + 1):
            if tickets[i] <= tickets[k]:
                ans += tickets[i]
            else:
                ans += tickets[k]
        # right side
        for i in range(k + 1, len(tickets)):
            if tickets[i] >= tickets[k]:
                ans += tickets[k] - 1
            else:
                ans += tickets[i]
        return ans