class Solution:
    def circularArrayLoop(self, nums: List[int]) -> bool:
        visited = set()
        leng = len(nums)
        for i in range(leng):
            if i not in visited:
                checked = set()
                while True:
                    if i in checked:
                        return True
                    checked.add(i)
                    visited.add(i)
                    prev, i = i, (i + nums[i]) % leng
                    if nums[prev] > 0 != nums[i] < 0:
                        break
                    if prev == i:
                        break

        return False