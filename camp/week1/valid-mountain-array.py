class Solution:
    def validMountainArray(self, arr: List[int]) -> bool:
        if len(arr) < 3:
            return False
        if arr[0] > arr[1]:
            return False
        up = True
        for i in range(1,len(arr)):
            if arr[i] == arr[i-1]:
                return False
            if up and arr[i] > arr[i-1]:
                continue
            if up and arr[i] < arr[i-1]:
                up = False
                continue
            if not up:
                if arr[i] > arr[i-1]:
                    return False
        if up:
            return False
        return True