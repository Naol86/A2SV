# Problem: String Compression - https://leetcode.com/problems/string-compression/

class Solution:
    def compress(self, chars: List[str]) -> int:
        last = chars[0]
        ans = [last]
        count = 1
        i = 1
        while i < len(chars):
            if chars[i] != last:
                if count != 1:
                    temp = str(count)
                    for j in range(len(temp)):
                        ans.append(temp[j])
                count = 1
                last = chars[i]
                ans.append(last)
            else:
                count +=1
            i+=1
        if count != 1:
            temp = str(count)
            for j in range(len(temp)):
                ans.append(temp[j])
        for k in range(len(ans)):
            chars[k] = ans[k]
        chars = chars[:k+1]
        # print(chars)
        return len(ans)