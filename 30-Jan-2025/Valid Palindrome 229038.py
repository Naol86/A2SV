# Problem: Valid Palindrome - https://leetcode.com/problems/valid-palindrome/description/

class Solution:
    def isPalindrome(self, s: str) -> bool:
        a = 0
        b = len(s) -1
        while a < b:
            if not s[a].isalpha() and not s[a].isdigit() or s[a] == " ":
                a+=1
                continue
            if not s[b].isalpha() and not s[b].isdigit() or s[b] == " ":
                b-=1
                continue
            elif s[a].lower() != s[b].lower():
                return False
            else:
                a+=1
                b-=1
                
        return True