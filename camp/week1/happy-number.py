class Solution:
    def isHappy(self, n: int) -> bool:
        if n == 1:
            return True
        elif n < 7:
            return False
        temp = str(n)
        _sum = 0
        for i in temp:
            _sum += int(i)**2
        return self.isHappy(_sum)
        