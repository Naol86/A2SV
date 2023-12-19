class Solution:
    def maxScoreIndices(self, nums: List[int]) -> List[int]:
        one_sum = sum(nums)
        zero_sum = 0
        _max = one_sum
        _index = [0]
        for i in range(len(nums)):
            if nums[i] == 0:
                zero_sum += 1
                temp = one_sum + zero_sum
                if temp == _max:
                    _index.append(i+1)
                elif temp > _max:
                    _index = [i+1]
                    _max = temp
            else:
                one_sum -= 1
        return _index
