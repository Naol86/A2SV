class Solution:
    def minOperations(self, boxes: str) -> List[int]:
        ans = []
        leng = len(boxes)
        for i in range(leng):
            temp = 0
            for j in range(leng):
                if i == j:
                    continue
                if boxes[j] == '1':
                    temp += abs(i-j)
            ans.append(temp)
        return ans