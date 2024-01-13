class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        leng = len(fruits)
        if leng == 1:
            return 1
        _dict = defaultdict(int)
        _dict[fruits[0]] += 1
        _dict[fruits[1]] += 1
        _max = 2
        left = 0
        right = 2
        while right < leng:
            if fruits[right] in _dict or len(_dict) == 1:
                _dict[fruits[right]] += 1
                right += 1
                _max = max(_max,right-left)
            elif _dict[fruits[left]] == 1:
                _dict.pop(fruits[left])
                left +=1
                _dict[fruits[right]] += 1
                right += 1
            else:
                _dict[fruits[left]] -= 1
                left += 1
        return _max
