class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        g.sort()
        s.sort()
        g_index, g_leng = 0, len(g)
        s_index, s_leng = 0, len(s)
        count = 0
        while g_index < g_leng and s_index < s_leng:
            if s[s_index] >= g[g_index]:
                count += 1
                s_index += 1
                g_index += 1
            else:
                s_index += 1
        return count