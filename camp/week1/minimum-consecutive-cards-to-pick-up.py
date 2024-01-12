class Solution:
    def minimumCardPickup(self, cards: List[int]) -> int:
        _dict = defaultdict(int)
        left = 0
        right = 0
        _min = float('inf')
        while right < len(cards):
            if _dict[cards[right]] >= 2:
                if cards[left] == cards[right]:
                    right += 1
                else:
                    _min = min(_min, right - left)
                _dict[cards[left]] -= 1
                left += 1
            else:
                _dict[cards[right]] += 1
                if _dict[cards[right]] == 2:
                    _min = min(_min, right - left + 1)
                else:
                    right += 1
        if _min == float('inf'):
            return -1
        return _min