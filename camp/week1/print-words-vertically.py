class Solution:
    def printVertically(self, s: str) -> List[str]:
        lis = s.split()
        _max = 0
        for i in lis:
            if len(i) > _max:
                _max = len(i)

        vertically_list = []
        for i in range(_max):
            ans = ""
            for j in range(len(lis)):
                if len(lis[j]) > i:
                    ans += lis[j][i]
                else:
                    ans += " "
            vertically_list.append(ans.rstrip())
        return vertically_list