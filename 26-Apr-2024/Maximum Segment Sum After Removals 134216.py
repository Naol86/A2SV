# Problem: Maximum Segment Sum After Removals - https://leetcode.com/problems/maximum-segment-sum-after-removals/description/

class Solution:
    def maximumSegmentSum(self, nums: List[int], removeQueries: List[int]) -> List[int]:
        ans = [0]
        parent = {}
        rep = defaultdict(int) # representation and sum
        x = len(nums)
        destroy = removeQueries

        visited = set()
        _max = 0

        def find(x):
            if x not in visited:
                return -1
            if x == parent[x]:
                return x
            parent[x] = find(parent[x])
            return parent[x]

        def union(x, y):
            parentX = find(x)
            parentY = find(y)
            if parentX == parentY:
                return rep[parentX]
            parent[parentY] = parentX
            rep[parentX] += rep[parentY]
            return rep[parentX]

        for i in range(x-1, 0, -1):
            visited.add(destroy[i])
            temp = nums[destroy[i]]
            rep[destroy[i]] = temp
            parent[destroy[i]] = destroy[i]
            left = find(destroy[i] - 1)
            right = find(destroy[i] + 1)
            # print(destroy[i], left, right)
            if left != -1 and right != -1:
                union(left, destroy[i])
                temp = union(left, right)
            if right == -1 and left != -1:
                temp = union(left, destroy[i])
            if left == -1 and right != -1:
                # print('parent ',parent)
                temp = union(right, destroy[i])
                # print("here i am", right, destroy[i], dict(rep))
            # print(dict(parent))
            # print(dict(rep))
            # print('--------------')
            _max = max(_max, temp)
            ans.append(_max)
        return ans[::-1]