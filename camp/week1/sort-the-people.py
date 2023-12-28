class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        dic = {}
        leng = len(names)
        for i in range(leng):
            dic[heights[i]] = i
        heights.sort(reverse= True)
        ans = []
        for i in heights:
            ans.append(names[dic[i]])
        return ans
