class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        _min = 0
        for i in range(k):
            if blocks[i] == "W":
                _min += 1
        
        left = 0
        right = k
        pre = _min
        while right < len(blocks):
            temp = pre
            if blocks[left] == "W":
                temp -= 1
            if blocks[right] == "W":
                temp += 1
            _min = min(_min, temp)
            pre = temp
            left += 1
            right += 1
        return _min
        