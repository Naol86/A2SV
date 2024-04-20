# Problem: Single-Threaded CPU - https://leetcode.com/problems/single-threaded-cpu/

class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:
        for i in range(len(tasks)):
            tasks[i] = [tasks[i][1], i, tasks[i][0]]
        tasks.sort(key=lambda x: x[2])
        # print(tasks)

        heap = []
        ans = []
        time = tasks[0][2]
        i = 0
        while i < len(tasks) and tasks[i][2] == time:
            heapq.heappush(heap, tasks[i])
            i += 1
        while heap:
            a, b, c = heapq.heappop(heap)
            ans.append(b)
            time += a
            while i < len(tasks):
                if tasks[i][2] <= time:
                    heapq.heappush(heap, tasks[i])
                else:
                    # heapq.heappush(heap, tasks[i])
                    break
                i += 1
            if not heap and i < len(tasks):
                time = tasks[i][2]
                while i < len(tasks) and tasks[i][2] == time:
                    heapq.heappush(heap, tasks[i])
                    i += 1
            
        return ans 
        