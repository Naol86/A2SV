class TopVotedCandidate:

    def __init__(self, persons: List[int], times: List[int]):
        self.persons = persons
        self.times = times
        _max = 0
        peron = self.persons[0]
        _dict = defaultdict(int)
        for i in range(len(self.persons)):
            _dict[self.persons[i]] += 1
            if _dict[self.persons[i]] >= _max:
                _max = _dict[self.persons[i]]
                person = self.persons[i]
            self.persons[i] = person
        # print(self.persons)
        

    def q(self, t: int) -> int:
        x = bisect.bisect_right(self.times, t)
        return self.persons[x - 1]
        


# Your TopVotedCandidate object will be instantiated and called as such:
# obj = TopVotedCandidate(persons, times)
# param_1 = obj.q(t)