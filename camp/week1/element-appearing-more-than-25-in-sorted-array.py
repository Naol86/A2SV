class Solution:
    def findSpecialInteger(self, arr: List[int]) -> int:
        dic = {}
        leng = len(arr)
        for i in arr:
            if i in dic:
                dic[i] += 1
                if dic[i] > leng *0.25:
                    return i
            else:
                dic[i] = 1
                if dic[i] > leng*0.25:
                    return i
        return -1