import math
class Solution:
    def numberOfMatches(self, n: int) -> int:
        _sum = 0
        # if n % 2 != 0:
            # _sum += n
        while n > 0:
            _sum += n//2
            if n/2 >= 1:
                n = math.ceil(n/2)
            else:
                break
        return _sum