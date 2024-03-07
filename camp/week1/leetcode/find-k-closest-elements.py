class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        left = bisect.bisect_left(arr, x)
        right = bisect.bisect_right(arr, x)
        if right - left >= k:
            # print('here')
            # arr = arr[left:right]
            return arr[left:right][:k]
        queue = deque(arr[left:right])
        k -= right - left
        left -= 1
        while k > 0:
            # print(queue, left, right)
            l = abs(arr[left] - x) if left >= 0 else float('inf')
            r = abs(arr[right] - x) if right < len(arr) else float('inf')
            if l == float('inf') and r == float('inf'):
                break
            if l <= r:
                queue.appendleft(arr[left])
                left -= 1
            else:
                queue.append(arr[right])
                right += 1
            k -= 1
        # print(queue)
        return list(queue)