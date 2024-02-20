class Solution:
    def breakPalindrome(self, palindrome: str) -> str:
        lis = [i for i in palindrome]
        if len(lis) == 1:
            return ""
        for i in range(len(lis)):
            if lis[i] > 'a' and lis[len(lis) - i - 1] != 'a' and i != len(lis)//2:
                lis[i] = 'a'
                return ''.join(lis)
        if lis[-1] == 'a':
            lis[-1] = 'b'
            return ''.join(lis)
        return ''