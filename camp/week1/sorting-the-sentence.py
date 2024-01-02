class Solution:
    def sortSentence(self, s: str) -> str:
        lis=s.split()
        di={}
        for i in lis:
            ind=[]
            for j in range(len(i)-1,0,-1):
                if not i[j].isdigit():
                    break
                ind.insert(0,i[j])
            st=''.join(ind)
            di[int(st)]=i[:0-len(st)]
        Index=sorted(di)
        ans=''
        for i in Index:
            ans=ans+di[i]+' '
        ans=ans[:-1]
        return ans