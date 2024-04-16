# Problem: Snakes and Ladders - https://leetcode.com/problems/snakes-and-ladders/

class Solution:
    def snakesAndLadders(self, board: List[List[int]]) -> int:
        lis = [0]
        j = 0
        for i in range(len(board) - 1, -1, -1):
            if j % 2 == 1:
                lis.extend(board[i][::-1])
            else:
                lis.extend(board[i])
            j += 1
        # print(lis)
        # print(len(lis))
        queue = deque([(1,0)])
        visited = set([1])
        while queue:
            leng = len(queue)
            for _ in range(leng):
                node, level = queue.popleft()
                # count = 0
                for i in range(1,7):
                    if node + i in visited:
                        continue
                    if node + i >= len(lis) - 1:
                        return level + 1
                    visited.add(node + i)
                    if lis[node + i] != -1:
                        if lis[node + i] == len(lis) - 1:
                            return level + 1  
                        queue.append((lis[node + i], level + 1))
                        # if lis[node + i] <= node + i:
                        #     print(lis[node + i], node + i)
                        #     count += 1

                        continue
                    queue.append((node + i, level + 1))
                # if count == 6:
                #     print('here')
                #     # return -1
        return -1