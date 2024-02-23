class Solution:
    def deckRevealedIncreasing(self, deck: List[int]) -> List[int]:
        deck.sort()
        if len(deck) < 3:
            return deck
        queue = deque([i for i in range(len(deck))])
        ans = [0] * len(deck)
        count = 0
        while len(queue) > 1:
            x = queue.popleft()
            queue.append(queue.popleft())
            ans[x] = deck[count]
            count += 1
        if queue:
            ans[queue.pop()] = deck[count]
        return ans