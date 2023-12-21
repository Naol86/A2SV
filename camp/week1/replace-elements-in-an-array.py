class Solution:
    def arrayChange(self, nums: List[int], operations: List[List[int]]) -> List[int]:
        dic = defaultdict(int)
        for i in range(len(nums)):
            dic[nums[i]] += i
        for i in operations:
            nums[dic[i[0]]] = i[1]
            dic[i[1]] = dic[i[0]]
            dic.pop(i[0])
        return nums