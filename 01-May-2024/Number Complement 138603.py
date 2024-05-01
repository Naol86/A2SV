# Problem: Number Complement - https://leetcode.com/problems/number-complement/

class Solution:
    def findComplement(self, num: int) -> int:
        # num = ~num
        # add = 0
        # if num & (num-1) == 0:
        #     add = 1
        # x = math.ceil(math.log2(num)) + add
        # print(~num, x)
        return num ^ ((1 << num.bit_length()) - 1)