class Solution:
    def minWindow(self, s: str, t: str) -> str:
        leng = len(s)
        t_dict = Counter(t)
        _min = s
        check = True
        t_set = {i:1 for i in t_dict.keys()}
        s_dict = defaultdict(int)
        s_set = {}
        right = left = 0
        while right <= leng:
            if s_set == t_set and left < right:
                _min = _min if len(_min) <= right - left else s[left:right]
                check = False
                s_dict[s[left]] -= 1
                if s_dict[s[left]] < t_dict[s[left]]:
                    if s[left] in s_set:
                        s_set.pop(s[left])
                    if s_dict[s[left]] == 0:
                        s_dict.pop(s[left])
                left += 1
            elif right < leng and s[right] in t_set:
                s_dict[s[right]] += 1
                if s_dict[s[right]] >= t_dict[s[right]]:
                    s_set[s[right]] = 1
                right += 1
            else:
                right += 1
        if check:
            return ""
        return _min
