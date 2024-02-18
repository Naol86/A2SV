class Solution:
    def numRabbits(self, answers: List[int]) -> int:
        temp = {}
        ans = 0
        for answer in answers:
            if answer not in temp:
                ans += answer + 1
                temp[answer] = 1
            else:
                temp[answer] += 1
                if temp[answer] > answer + 1:
                    ans += answer + 1
                    temp[answer] = 1
        return ans