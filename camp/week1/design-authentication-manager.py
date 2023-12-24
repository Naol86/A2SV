class AuthenticationManager:

    def __init__(self, timeToLive: int):
        self.time = timeToLive
        self.tokens = defaultdict(list)

    def generate(self, tokenId: str, currentTime: int) -> None:
        self.tokens[tokenId] = [currentTime, currentTime + self.time]

    def renew(self, tokenId: str, currentTime: int) -> None:
        if tokenId in self.tokens:
            if currentTime < self.tokens[tokenId][1]:
                self.tokens[tokenId] = [currentTime, currentTime + self.time]
        

    def countUnexpiredTokens(self, currentTime: int) -> int:
        count = 0
        for key, value in self.tokens.items():
            if currentTime < value[1]:
                count += 1
            # else:
                # self.tokens.pop(key)
        return count


# Your AuthenticationManager object will be instantiated and called as such:
# obj = AuthenticationManager(timeToLive)
# obj.generate(tokenId,currentTime)
# obj.renew(tokenId,currentTime)
# param_3 = obj.countUnexpiredTokens(currentTime)