# Problem: Splitting a String Into Descending Consecutive Values - https://leetcode.com/problems/splitting-a-string-into-descending-consecutive-values/

class Solution:
    def splitString(self, s: str) -> bool:
        ans = []
        final = []
        s = [i for i in s]
        def back_tracking(lis, prev):
            if lis >= len(s):
                # print('s', ans)
                if len(ans) > 1:
                    for i in range(1, len(ans)):
                        if ans[i - 1] - 1 != ans[i]:
                            return False
                    final.append(ans.copy())
                    return True
                return False
            for i in range(lis, len(s)):
                # print(lis, prev)
                temp = int(''.join(s[lis:i+1]))
                if prev is not None and prev <= temp:
                    # print("break")
                    break
                elif prev is not None and prev - 1 > temp:
                    continue
                # print(temp)
                ans.append(temp)
                back = back_tracking(i + 1, temp)
                ans.pop()
                if back:
                    return True
            return False

        # back_tracking(s, None)
        # print(final)
        return back_tracking(0, None)