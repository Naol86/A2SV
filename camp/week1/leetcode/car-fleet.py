class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        _list = [(position[i], speed[i]) for i in range(len(position))]
        _list.sort()
        lis = []
        ans=0
        for i in range(len(position)):
            lis.append((target - _list[i][0]) / _list[i][1])
        print(lis)
        stack = [lis[0]]
        for i in range(1, len(lis)):
            if lis[i] < stack[-1]:
                stack.append(lis[i])
            else:
                while stack and stack[-1] <= lis[i]:
                    stack.pop()
                stack.append(lis[i])
        return len(stack)
        