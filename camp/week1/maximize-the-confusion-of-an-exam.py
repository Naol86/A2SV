class Solution:
    def maxConsecutiveAnswers(self, answerKey: str, k: int) -> int:
        _max = 0
        t = k
        a = 0
        b = 0
        while b < len(answerKey):
            if answerKey[b] == 'T':
                b += 1
            elif answerKey[b] == 'F':
                if t == 0:
                    _max = max(_max, b - a)
                    while t == 0:
                        if answerKey[a] == 'F':
                            t += 1
                        a += 1
                else:
                    t -= 1
                    b += 1
        _max = max(_max, b - a)
        _max_f = 0
        t = k
        a = 0
        b = 0
        while b < len(answerKey):
            if answerKey[b] == 'F':
                b += 1
            elif answerKey[b] == 'T':
                if t == 0:
                    _max_f = max(_max_f, b - a)
                    while t == 0:
                        if answerKey[a] == 'T':
                            t += 1
                        a += 1
                else:
                    t -= 1
                    b += 1
        _max_f = max(_max_f, b - a)
        return max(_max_f, _max)

