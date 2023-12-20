class Solution:
    def check(self, num):
        count = 0
        while (3**count) <= num:
            count +=1
        return count - 1
    def checkPowersOfThree(self, n: int) -> bool:
        power_set = set([])
        while n:
            if n < 0:
                return False
            temp = self.check(n)
            if temp in power_set or temp < 0:
                return False
            power_set.add(temp)
            n -= (3**temp)
        return True