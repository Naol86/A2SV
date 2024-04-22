# Problem: Meeting Rooms III - https://leetcode.com/problems/meeting-rooms-iii/

class Solution:
    def mostBooked(self, n: int, meetings: List[List[int]]) -> int:
        # if len(meetings) <= n:
        #     return 0
        ans = [0] * n
        meetings.sort()
        # print(meetings)
        heap = []
        i = 0
        room = [i for i in range(n)]
        for start, end in meetings:
            while heap and heap[0][0] <= start:
                e, indx = heapq.heappop(heap)
                heapq.heappush(room, indx)
            if len(heap) < n:
                use = heapq.heappop(room)
                heapq.heappush(heap, (end, use))
                ans[use] += 1
            else:
                e, indx = heapq.heappop(heap)
                heapq.heappush(heap, (e + end - start, indx))
                ans[indx] += 1
            # print(room)

        # print(ans)

        return ans.index(max(ans))            
            