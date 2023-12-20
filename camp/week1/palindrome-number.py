class Solution:
    def isPalindrome(self, x: int) -> bool:
        temp = str(x)
        temp2 = str(x)[::-1]
        if temp == temp2 :
            return True 
        else:
            return False
        