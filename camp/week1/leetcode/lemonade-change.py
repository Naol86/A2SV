class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        note = {5:0, 10:0}
        for bill in bills:
            if bill == 5:
                note[5] += 1
            else:
                if note[5] < 1:
                    return False
                if bill == 10:
                    note[5] -= 1
                    note[10] += 1
                else:
                    if note[10] > 0:
                        note[10] -= 1
                        note[5] -= 1
                    elif note[5] > 2:
                        note[5] -= 3
                    else:
                        return False
        return True