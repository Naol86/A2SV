class Solution:
    def predictTheWinner(self, nums: List[int]) -> bool:
        def back_tracking(array, turn):
            if len(array) == 0:
                return 0
            a = array[0] - back_tracking(array[1:], not turn)
            b = array[-1] - back_tracking(array[:-1], not turn)
            return max(a, b)
        ans = (back_tracking(nums, True))
        if ans < 0:
            return False
        return True