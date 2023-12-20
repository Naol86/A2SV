class Solution:
    def average(self, salary: List[int]) -> float:
        salary.sort()
        aver = sum(salary[1:-1])/len(salary[1:-1])
        return aver