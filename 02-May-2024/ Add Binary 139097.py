# Problem:  Add Binary - https://leetcode.com/problems/add-binary/

class Solution:
    def addBinary(self, a: str, b: str) -> str:
        lenA = len(a)
        lenB= len(b)
        Max = lenA if lenA>=lenB else lenB
        a = (Max - len(a)) * '0' + a
        b = (Max - len(b)) * '0' + b
        ans = ''
        carry = 0
        for i in range(Max-1,-1,-1):
            Sum = carry ^ int(a[i]) ^ int(b[i])
            carry = (int(a[i]) & int(b[i])) | (carry & int(a[i])) | (carry & int(b[i]))
            ans = str(Sum) + ans
        if carry == 1:
            return '1'+ans
        else:
            return ans