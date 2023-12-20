class Solution:
    def wateringPlants(self, plants: List[int], capacity: int) -> int:
        distance = 0
        total_distance = 0
        reminder = capacity
        i = -1
        leng = len(plants)
        while i < leng - 1:
            i += 1
            if plants[i] <= reminder:
                reminder -= plants[i]
                distance += 1
                total_distance += 1
            else:
                total_distance += distance * 2 + 1
                print(distance)
                reminder = capacity - plants[i]
                distance += 1
        return total_distance