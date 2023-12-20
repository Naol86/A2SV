class Solution:
    def escapeGhosts(self, ghosts: List[List[int]], target: List[int]) -> bool:
        my_dis = abs(target[0]) + abs(target[1])
        print(my_dis)
        for i in ghosts:
            ghost_dis = abs(target[0]-i[0]) + abs(target[1] - i[1])
            if ghost_dis <= my_dis:
                return False
        return True