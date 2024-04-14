# Problem: Open the Lock - https://leetcode.com/problems/open-the-lock/

class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        deadend = set()
        for a, b, c, d in deadends:
            deadend.add((int(a), int(b), int(c), int(d)))
        target = (int(target[0]),int(target[1]),int(target[2]),int(target[3]))
        if (0,0,0,0) in deadend:
            return -1
        # print(deadend)
        queue = deque([(0,0,0,0)])
        visited = set([(0,0,0,0)])
        def find(lis, i):
            temp = deepcopy(lis)
            temp[i] = (temp[i] + 1) % 10
            temp = tuple(temp)
            if temp not in visited and temp not in deadend:
                queue.append(temp)
                visited.add(temp)
            if lis[i] == 0:
                lis[i] = 9
            else:
                lis[i] -= 1
            lis = tuple(lis)
            if lis not in visited and lis not in deadend:
                queue.append(lis)
                visited.add(lis)

        level = 0
        while queue:
            leng = len(queue)
            for _ in range(leng):
                a, b, c, d = queue.popleft()
                if (a, b, c, d) == target:
                    print((a, b, c, d))
                    return level
                for i in range(4):
                    find([a, b, c, d], i)
                # print(queue)
            level += 1
        return -1