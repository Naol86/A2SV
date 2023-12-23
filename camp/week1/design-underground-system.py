class UndergroundSystem:

    def __init__(self):
        self.passenger = defaultdict(list)
        self.station = defaultdict(list)

    def checkIn(self, id: int, stationName: str, t: int) -> None:
        self.passenger[id] = [stationName, t]

    def checkOut(self, id: int, stationName: str, t: int) -> None:
        name = self.passenger[id][0] + "-" + stationName
        time = t - self.passenger[id][1]
        if name not in self.station:
            self.station[name] = [time, 1]
        else:
            self.station[name][0] += time
            self.station[name][1] += 1
        self.passenger[id] = [stationName, t] 
        

    def getAverageTime(self, startStation: str, endStation: str) -> float:
        name = startStation + "-" + endStation
        temp = self.station[name]
        return temp[0] / temp[1]


# Your UndergroundSystem object will be instantiated and called as such:
# obj = UndergroundSystem()
# obj.checkIn(id,stationName,t)
# obj.checkOut(id,stationName,t)
# param_3 = obj.getAverageTime(startStation,endStation)