class Bitset:

    def __init__(self, size: int):
        self.size = size
        self.one_num = 0
        self.bit = "0" * size
        self.bit_flip = "1" * size

    def fix(self, idx: int) -> None:
        if self.bit[idx] == "0":
            self.one_num += 1
        self.bit = self.bit[:idx] + "1" + self.bit[idx+1:]
        self.bit_flip = self.bit_flip[:idx] + "0" + self.bit_flip[idx+1:]

    def unfix(self, idx: int) -> None:
        if self.bit[idx] == "1":
            self.one_num -= 1
        self.bit = self.bit[:idx] + "0" + self.bit[idx+1:]
        self.bit_flip = self.bit_flip[:idx] + "1" + self.bit_flip[idx+1:]

    def flip(self) -> None:
        self.one_num = self.size - self.one_num
        temp = self.bit
        self.bit = self.bit_flip
        self.bit_flip = temp

    def all(self) -> bool:
        if self.size == self.one_num:
            return True
        return False

    def one(self) -> bool:
        if self.one_num > 0:
            return True
        return False

    def count(self) -> int:
        return self.one_num

    def toString(self) -> str:
        return self.bit