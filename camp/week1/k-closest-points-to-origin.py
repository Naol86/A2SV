import heapq
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        lis = []
        for i in range(k):
            temp = math.sqrt((points[i][0] ** 2) + (points[i][1] ** 2))
            lis.append((-temp,points[i]))
        heapq.heapify(lis)
        for point in points[k:]:
            temp = math.sqrt((point[0] ** 2) + (point[1] ** 2))
            if lis[0][0] < -temp:
                heapq.heappop(lis)
                heapq.heappush(lis,(-temp,point))
        ans = []
        for i in lis:
            ans.append(i[1])
        return ans
            