class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        ans = "{"
        for i in letters:
            if i > target and i < ans:
                ans = i
        if ans == "{":
            return letters[0]
        return ans