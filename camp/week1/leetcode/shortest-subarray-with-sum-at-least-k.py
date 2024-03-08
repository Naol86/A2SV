class Solution:
    def shortestSubarray(self, nums: List[int], k: int) -> int:
        start = 0
        for i in range(len(nums)):
            if nums[i] > 0:
                start = i
                break
        queue = deque([(0, start - 1)])
        _sum = 0
        leng = float('inf')
        for i in range(start, len(nums)):
            _sum += nums[i]
            # print(i)
            if _sum <= 0:
                queue = deque([(0, i)])
                _sum = 0
                continue
            while queue and _sum - queue[0][0] >= k:
                x = queue.popleft()
                leng = min(leng, i - x[1])
                # _sum -= x[0]
                # print(queue)
            while queue and queue[-1][0] > _sum:
                queue.pop()
                # print(queue)
            queue.append((_sum, i))
            # print(queue)
        if leng == float('inf'):
            return -1
        return leng
