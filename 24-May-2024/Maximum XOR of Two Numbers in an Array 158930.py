# Problem: Maximum XOR of Two Numbers in an Array - https://leetcode.com/problems/maximum-xor-of-two-numbers-in-an-array/

class TrieNode:
    def __init__(self):
        self.children = [None] * 2

class Solution:
    def __init__(self):
        self.root = TrieNode()
    
    def insert(self, num) -> None:
        i = 31
        cur = self.root
        while i >= 0:
            w = 1 if num & (1<<i) else 0
            if not cur.children[w]:
                cur.children[w] = TrieNode()
                cur = cur.children[w]
            else:
                cur = cur.children[w]
            i-=1
    
    def find(self, num):
        
        x = 0
        i = 31
        cur = self.root
        while i >= 0 and cur:
            w = 1 if num & (1<<i) else 0
            if cur.children[(w+1)%2]:
                cur = cur.children[(w+1)%2]
                x += (1<<i) * ((w+1)%2)
            else:
                cur = cur.children[w]
                x += (1<<i) * w
            i -= 1

        return x

    def findMaximumXOR(self, nums: List[int]) -> int:
        for num in nums:
            self.insert(num)
        ans = 0
        for num in nums:
            ans = max(ans, num ^ self.find(num))
        
        return ans

        