class Solution:
    def distanceBetweenBusStops(self, distance: List[int], start: int, destination: int) -> int:
        dis1 = 0
        leng = len(distance)
        i = start
        while i != destination:
            dis1 += distance[i]
            i = (i+1)%leng
        dis2 = 0
        i = start
        while i != destination and i != (destination - leng - 1):
            dis2 += distance[i-1]
            i = (i-1)%leng
        return min(dis1, dis2)
