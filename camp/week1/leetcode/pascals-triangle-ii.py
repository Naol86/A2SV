class Solution:

    def getRow(self, rowIndex: int) -> List[int]:
        raw = [1]
        def help(n, raw):
            if n == 0:
                return raw
            temp = [1]
            for i in range(len(raw) - 1):
                temp.append(raw[i] + raw[i + 1])
            temp.append(1)
            return help(n - 1, temp)
        return help(rowIndex, raw)