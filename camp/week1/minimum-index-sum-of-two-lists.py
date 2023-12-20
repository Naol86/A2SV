class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        _min = 2002
        dic = {}
        ans = []
        for i in range(len(list1)):
            dic[list1[i]] = i
        for i in range(len(list2)):
            if list2[i] in dic:
                if i + dic[list2[i]] < _min:
                    ans = [list2[i]]
                    _min = i  + dic[list2[i]]
                elif i + dic[list2[i]] == _min:
                    ans.append(list2[i])
        return ans
