# Problem: Find Original Array From Doubled Array (Optional) - https://leetcode.com/problems/find-original-array-from-doubled-array/

class Solution:
    def findOriginalArray(self, changed: List[int]) -> List[int]:
        if len(changed) % 2:
            return []
        changed.sort()
        # _set = set(changed)
        count = Counter(changed)
        print(count)
        ans = []
        for i in range(len(changed)):
            if changed[i] not in count:
                continue
            if changed[i] * 2 not in count:
                return []
            ans.append(changed[i])
            count[changed[i] * 2] -= 1
            count[changed[i]] -= 1
            if count[changed[i] * 2] == 0:
                count.pop(changed[i] * 2)
            # print(count, changed[i])
            if changed[i] in count and count[changed[i]] == 0:
                count.pop(changed[i])
                pass
        if len(ans) != len(changed)//2:
            return []
        return ans