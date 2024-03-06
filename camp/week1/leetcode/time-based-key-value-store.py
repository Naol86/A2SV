class TimeMap:

    def __init__(self):
        self._dict = defaultdict(list)
        
    def set(self, key: str, value: str, timestamp: int) -> None:
        self._dict[key].append((timestamp, value))
        
    def get(self, key: str, timestamp: int) -> str:
        # print(self._dict)
        lis = self._dict[key]
        if lis == []:
            return ""
        left = 0
        right = len(lis) - 1
        ans = 0
        while left <= right:
            mid = left + (right - left) // 2

            if lis[mid][0] <= timestamp:
                ans = mid
                left = mid + 1
            else:
                right = mid - 1
        if timestamp < lis[ans][0]:
            return ""
        # print(ans)
        # print(lis)
        return lis[ans][1]



# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)