class FrequencyTracker:

    def __init__(self):
        self.list = defaultdict(int)
        self.frequency = defaultdict(int)

    def add(self, number: int) -> None:
        if number in self.list and self.list[number] > 0:
            self.frequency[self.list[number]] -= 1
        self.list[number] += 1
        self.frequency[self.list[number]] += 1

    def deleteOne(self, number: int) -> None:
        if number not in self.list or self.list[number] == 0:
            return
        self.frequency[self.list[number]] -= 1
        self.list[number] -= 1
        self.frequency[self.list[number]] += 1
        

    def hasFrequency(self, frequency: int) -> bool:
        if self.frequency[frequency] > 0:
            return True
        return False