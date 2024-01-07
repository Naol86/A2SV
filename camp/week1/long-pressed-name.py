from collections import Counter

class Solution:
    def isLongPressedName(self, name: str, typed: str) -> bool:
        leng = len(name)
        if leng > len(typed):
            return False
        point = 0
        temp = 0
        while point < leng and temp < len(typed):
            if name[point] == typed[temp]:
                point += 1
                temp += 1
            elif temp > 0 and typed[temp] == typed[temp - 1]:
                temp += 1
            else:
                return False
        if point != leng:
            return False
        for i in range(temp, len(typed)):
            if typed[i] != name[-1]:
                return False
        return True