class Solution:
    def countPairs(self, nums: List[int], k: int) -> int:
        dic = defaultdict(list)
        count = 0
        for i in range(len(nums)):
            if nums[i] not in dic:
                dic[nums[i]].append(i)
                continue
            for j in dic[nums[i]]:
                if (j * i) % k == 0:
                    count += 1
            dic[nums[i]].append(i)
            
        return count