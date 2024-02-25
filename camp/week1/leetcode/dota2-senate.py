class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        r_queue = deque()
        d_queue = deque()

        leng = len(senate)
        for i in range(leng):
            if senate[i] == 'R':
                r_queue.append(i)
            else:
                d_queue.append(i)

        while r_queue and d_queue:
            if r_queue[0] < d_queue[0]:
                r_queue.append(r_queue.popleft() + leng)
                d_queue.popleft()
            else:
                d_queue.append(d_queue.popleft() + leng)
                r_queue.popleft()

        if r_queue:
            return "Radiant"
        return "Dire"
        