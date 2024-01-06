class Solution:
    def intervalIntersection(self, firstList: List[List[int]], secondList: List[List[int]]) -> List[List[int]]:
        ans = []
        upper = 0
        lower = 0
        while upper < len(firstList) and lower < len(secondList):
            # print(firstList[upper], secondList[lower])
            if firstList[upper][1] >= secondList[lower][0] and secondList[lower][1] >= firstList[upper][0]:
                temp = [max(firstList[upper][0], secondList[lower][0]),min(firstList[upper][1], secondList[lower][1])]
                # if temp[0] > 
                ans.append(temp)
                if temp[1] == firstList[upper][1]:
                    upper += 1
                else:
                    lower += 1
            elif firstList[upper][1] > secondList[lower][1]:
                lower += 1
            else:
                upper += 1
        return ans
                