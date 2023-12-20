class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        lis = s.copy()
        leg = len(lis) - 1
        for i in range(len(lis)):
            s[i] = lis[leg - i]