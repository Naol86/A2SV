class Solution:
    def convert(self, num):
        _sum = 0
        _index = -1
        for i in range(len(num)):
            digit = ord(num[_index]) - ord('1') + 1
            _sum += (10**i) * digit
            _index -= 1
        return _sum

    def multiply(self, num1: str, num2: str) -> str:
        num1 = self.convert(num1)
        num2 = self.convert(num2)
        return f"{num1 * num2}"