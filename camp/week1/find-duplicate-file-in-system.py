class Solution:
    def findDuplicate(self, paths: List[str]) -> List[List[str]]:
        dic = defaultdict(list)
        for i in paths:
            # print(i)
            lis = i.split()
            # print(lis)
            root = lis[0]
            for j in lis[1:]:
                # print(j)
                temp = j.split('(')
                # print(temp)
                name, content = temp[0], temp[1]
                dic[content].append(f"{root}/{name}")
        ans = []
        for i in dic:
            if len(dic[i]) > 1:
                ans.append(dic[i])
        return ans