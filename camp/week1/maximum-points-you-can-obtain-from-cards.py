class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        if len(cardPoints) == k:
            return sum(cardPoints)
        leng = k * 2
        temp = []
        temp.extend(cardPoints[-k:])
        temp.extend(cardPoints[:k])
        _sum = 0
        for i in range(k):
            _sum += temp[i]

        _max = _sum
        left = 0
        right = k
        while right < leng:
            _sum -= temp[left]
            _sum += temp[right]
            _max = max(_max, _sum)
            left += 1
            right += 1
        return _max