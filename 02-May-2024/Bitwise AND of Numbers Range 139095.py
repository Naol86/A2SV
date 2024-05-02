# Problem: Bitwise AND of Numbers Range - https://leetcode.com/problems/bitwise-and-of-numbers-range/

class Solution:
    def rangeBitwiseAnd(self, left: int, right: int) -> int:
        if right - left <= 1:
            return right & left
        l = left.bit_length()
        r = right.bit_length()
        if l == r:
            print('some')
            dis = right - left
            dis = dis.bit_length()
            for i in range(dis):
                right &= ~(1<<i)
                left |= (1<<i)
            return right & left
        # print(type(left))
        # print(math.log2(left))
        return 0