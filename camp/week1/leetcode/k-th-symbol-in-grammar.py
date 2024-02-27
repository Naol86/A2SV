class Solution:
    def kthGrammar(self, n: int, k: int) -> int:
        if n == 1:
            return 0
        def helper(level, pos, left):
            if level == 1:
                return 1 if left else 0
            base = pow(2, level - 1)
            if pos > base // 2:
                return helper(level - 1, pos - base // 2, not left)
            else:
                return helper(level - 1, pos, left)
        return helper(n, k, False)

