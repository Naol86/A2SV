class Solution:
    def dividePlayers(self, skill: List[int]) -> int:
        dic = {}
        Sum = math.ceil(sum(skill)/(len(skill)/2))
        lis = []
        count = 0
        for i in skill:
            if (i not in dic) or dic[i] == 0:
                if (Sum - i) in dic:
                    dic[Sum - i] += 1
                else:
                    dic[Sum - i] = 1
            else:
                count +=1
                dic[i] -= 1
                lis.append((Sum - i) * i)
        if count == len(skill)/2:
            return sum(lis)
        return -1