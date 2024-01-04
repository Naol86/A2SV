class Solution:
    def pancakeSort(self, arr: List[int]) -> List[int]:
        ans = []
        leng = len(arr)
        for i in range(leng):
            max_index = 0
            for j in range(leng - i):
                max_index = max_index if arr[max_index] >= arr[j] else j
            if max_index == leng - i - 1:
                continue
            if max_index == 0:
                ans.append(leng-i)
            else:
                ans.append(max_index+1)
                ans.append(leng-i)
            temp = arr[:max_index+1][::-1]
            arr = temp + arr[max_index + 1:]
            arr = arr[:leng-i][::-1] + arr[leng - i:]
        return ans