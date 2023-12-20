class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        lis = []
        for i in range(n):
            for j in range(2):
                lis.append(nums[(j*n) + i])
        return lis