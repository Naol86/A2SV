import bisect
class Solution:
    def numTimesAllBlue(self, flips: List[int]) -> int:
        _max = flips[0]
        count = 0
        leng = 1
        if leng == _max:
            count += 1
        for i in flips[1:]:
            _max = max(i,_max)
            leng += 1
            if _max == leng:
                count += 1
        return count

            
            