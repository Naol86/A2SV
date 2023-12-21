class Solution:
    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:
        left_list = []
        right_list = []
        pivot_list = []
        for i in nums:
            if i > pivot:
                right_list.append(i)
            elif i < pivot:
                left_list.append(i)
            else:
                pivot_list.append(i)
        return left_list + pivot_list + right_list