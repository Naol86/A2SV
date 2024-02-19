class Solution:
    def longestPalindrome(self, s: str) -> int:
        count = Counter(s)
        print(count)
        length = 0
        odd_length = 0
        for key, value in count.items():
            if value % 2 == 0:
                length += value
            else:
                length += value - 1
                odd_length = 1 
        return length + odd_length