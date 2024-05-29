# Problem: Find All People With Secret - https://leetcode.com/problems/find-all-people-with-secret/

class Solution:
    def findAllPeople(self, n: int, meetings: List[List[int]], firstPerson: int) -> List[int]:
        meetings.sort(key=lambda x: x[-1])
        people = set([0, firstPerson])
        meetings.append([0,0, 0])

        parent = {}
        size = {}
        def find(x):
            if x not in parent:
                parent[x] = x
                size[x] = [x]
            if x == parent[x]:
                return x
            x = find(parent[x])
            return x
        def union(x, y):
            par_x = find(x)
            par_y = find(y)
            if par_x != par_y:
                if len(size[par_x]) > len(size[par_y]):
                    parent[par_y] = par_x
                    size[par_x].extend(size[par_y])
                else:
                    parent[par_x] = par_y
                    size[par_y].extend(size[par_x])
        time = meetings[0][-1]
        i = 0
        while i < len(meetings) - 1:
            temp = set()
            while meetings[i][-1] == time:
                a, b, _ = meetings[i]
                union(a, b)
                if a in people or b in people:
                    union(0, a)
                    union(0, b)
                #     temp.add(a)
                i += 1
            time = meetings[i][-1]
            # for k in temp:
            #     par = find(k)
            people.update(set(size[find(0)]))
            parent = {}
            size = {}
        return list(people)