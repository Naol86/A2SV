from collections import defaultdict
# from functools import cmp_to_key
class Solution:
    def smallestNumber(self, num: int) -> int:
        if num < 0:
            lis = sorted(str(abs(num)), reverse = True)
            num = -1 * int(''.join(lis))
            return num
        lis = sorted(str(num))
        zero = 0
        i = 0
        if lis[0] == '0':
            for i in range(len(lis)):
                if lis[i] != '0':
                    break
                zero += 1
        ans = [lis[i]] + ['0'] * zero + lis[i+1:]
        return int(''.join(ans))
        