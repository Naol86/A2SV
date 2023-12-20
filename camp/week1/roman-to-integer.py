class Solution:
    def romanToInt(self, s: str) -> int:
        lis={'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}
        ans=[0]
        count=1
        for i in s:
            if ans[-1] == lis[i]:
                count+=1
            if ans[-1] != lis[i]:
                count=1
            if count>3:
                ans=[0]
                break
            if lis[i] <= ans[-1]:
                ans+=[lis[i]]
            else:
                cal=lis[i]-ans.pop()
                ans+=[cal]
        return sum(ans)
        