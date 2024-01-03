class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort()
        left = 0
        right = len(people) - 1
        boat = 0
        while left <= right:
            boat += 1
            if people[right] == limit:
                right -= 1
            elif people[right] + people[left] <= limit:
                right -= 1
                left += 1
            else:
                right -= 1
        return boat

