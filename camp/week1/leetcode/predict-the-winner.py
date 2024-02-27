class Solution:
    def predictTheWinner(self, nums: List[int]) -> bool:
        def back_tracking(array):
            if len(array) == 0:
                return 0
            a = array[0] - back_tracking(array[1:])
            b = array[-1] - back_tracking(array[:-1])
            return max(a, b)
        ans = back_tracking(nums)
        if ans < 0:
            return False
        return True