# Problem: Solving Questions with Brainpower - https://leetcode.com/problems/solving-questions-with-brainpower/

class Solution:
    def mostPoints(self, questions: List[List[int]]) -> int:
        points = [0] * len(questions)
        points[-1] = questions[-1][0]
        _max = points[-1]
        for i in range(len(questions) - 2, -1, -1):
            right = 0 if i + questions[i][-1] + 1 >= len(questions) else points[i + questions[i][-1] + 1]
            points[i] += max(questions[i][0] + right, points[i+1])
            _max = max(_max, points[i])
        return _max