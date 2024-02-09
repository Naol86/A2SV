class Solution:
    def bestClosingTime(self, customers: str) -> int:
        leng  = len(customers) + 2
        count_yes = [0] * leng
        count_no = [0] * leng
        y = n = 0
        for i in range(1, leng):
            if i < leng - 1 and customers[i - 1] == "Y":
                y += 1
            elif i < leng - 1:
                n += 1
            count_yes[i] = y
            count_no[i] = n
        # print(count_yes)
        # print(count_no)
        _min = leng
        ans = 0
        for i in range(1, leng):
            temp = count_yes[-1] - count_yes[i - 1]
            temp += count_no[i - 1]
            if temp < _min:
                _min = temp
                ans = i - 1
        return ans