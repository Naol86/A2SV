# Problem: Furthest Building You Can Reach - https://leetcode.com/problems/furthest-building-you-can-reach/

class Solution:
    def furthestBuilding(self, heights: List[int], bricks: int, ladders: int) -> int:
        pos = [[0,0]]
        for i in range(1, len(heights)):
            if heights[i - 1] >= heights[i]:
                pos[-1][-1] = i
            else:
                pos.append([heights[i] - heights[i - 1], i])
        print(pos)
        heap = []
        end = pos[0][1]
        i = 1
        while ladders > 0 and i < len(pos):
            heapq.heappush(heap, pos[i][0])
            ladders -= 1
            end = pos[i][-1]
            i += 1
        while bricks and i < len(pos):
            # print(pos, i)
            if heap:
                heapq.heappush(heap, pos[i][0])
            else:
                heapq.heappush(heap, pos[i][0])
            x = heapq.heappop(heap)
            if x <= bricks:
                bricks -= x
                end = pos[i][-1]
            else:
                break
            i += 1

        return end
            