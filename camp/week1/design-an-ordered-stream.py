from array import array
class OrderedStream:

    def __init__(self, n: int):
        self.list = [""] * n
        self.pointer = 0
        self.size = n

    def insert(self, idKey: int, value: str) -> List[str]:
        self.list[idKey-1] = value
        ans = []
        i = self.pointer
        while i < self.size:
            if self.list[i] == "":
                return ans
            else:
                ans.append(self.list[i])
                self.pointer += 1
            i+=1
        return ans


        


# Your OrderedStream object will be instantiated and called as such:
# obj = OrderedStream(n)
# param_1 = obj.insert(idKey,value)