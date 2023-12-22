class ATM:

    def __init__(self):
        self.notes = {0:0, 1:0, 2:0, 3:0, 4:0}

    def deposit(self, banknotesCount: List[int]) -> None:
        for i in range(5):
            self.notes[i] += banknotesCount[i]

    def withdraw(self, amount: int) -> List[int]:
        note = [20,50,100,200,500]
        i = 4
        lis = [0] * 5
        while i > -1:
            if note[i] <= amount and self.notes[i] > 0:
                temp = amount// note[i]
                if temp <= self.notes[i]:
                    lis[i] += temp
                    self.notes[i] -= temp
                    amount -= note[i] * temp
                else:
                    lis[i] += self.notes[i]
                    amount -= note[i] * self.notes[i]
                    self.notes[i] = 0
            else:
                i -= 1
        if amount != 0:
            for i in range(5):
                self.notes[i] += lis[i]
            return [-1]
        return lis

# Your ATM object will be instantiated and called as such:
# obj = ATM()
# obj.deposit(banknotesCount)
# param_2 = obj.withdraw(amount)