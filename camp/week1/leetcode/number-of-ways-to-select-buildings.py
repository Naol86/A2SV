class Solution:
    def numberOfWays(self, s: str) -> int:
        count = 0
        one = zero = no_zero = no_one = 0
        for i in s:
            if i == '0':
                zero += 1
                no_one += one
                count += no_zero
            else:
                one += 1    
                no_zero += zero 
                count += no_one
        return count