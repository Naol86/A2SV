class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        _max = max(candies)
        greatest_kid = []
        for i in candies:
            if i + extraCandies >= _max:
                greatest_kid.append(True)
            else:
                greatest_kid.append(False)
        return greatest_kid