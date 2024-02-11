class Solution:
    def distance(self, nums: List[int]) -> List[int]:
        _dict = defaultdict(list)
        leng = len(nums)
        for i in range(leng):
            _dict[nums[i]].append(i)

        for key, lis in _dict.items():
            temp = len(lis) + 1
            if temp == 2:
                nums[lis[0]] = 0
                continue
            x = [0] + lis
            for i in range(1, temp):
                x[i] += x[i - 1]
            x.append(x[-1])
            for i in range(1, temp):
                nums[lis[i - 1]] = (
                    (x[-1] - x[i - 1]) - (lis[i-1] * (temp - i - 1)) +
                    ((i - 1) * lis[i - 1] - x[i])
                )
        return nums