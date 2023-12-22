class Solution:
    def subdomainVisits(self, cpdomains: List[str]) -> List[str]:
        dic = defaultdict(int)
        for i in cpdomains:
            lis = i.split()
            domain = lis[1].split(".")
            for j in range(len(domain)):
                temp = ".".join(domain[j:])
                dic[temp] += int(lis[0])
        ans = []
        for i in dic:
            ans.append(f"{dic[i]} {i}")
        return ans