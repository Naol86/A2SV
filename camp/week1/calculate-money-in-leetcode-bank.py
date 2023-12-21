class Solution:
    def totalMoney(self, n: int) -> int:
        _week = n//7
        _days = n % 7
        _sum = 0
        if n > 6:
            _sum += 28 + (_week -1)*7
        if _sum > 28:
            _sum = (_week /2)*(28+_sum)
        for i in range(_week+1,_week+1+_days):
            _sum += i
                
        return int(_sum)
                
                
                
