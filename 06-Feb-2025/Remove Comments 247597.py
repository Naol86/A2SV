# Problem: Remove Comments - https://leetcode.com/problems/remove-comments/

class Solution:
    def removeComments(self, source: List[str]) -> List[str]:
        ans = []
        s = []
        multi = False
        for line in source:
            i = 0
            while i < len(line):
                if not multi:
                    if line[i] == '/':
                        if i + 1 < len(line) and line[i + 1] not in {'*', '/'}:
                            s.append(line[i])
                            i += 1
                            continue
                        if i + 1 < len(line) and line[i + 1] == '*':
                            multi = True
                            i += 2
                        elif i + 1 < len(line) and line[i + 1] == '/':
                            temp = ''.join(s)
                            print(temp)
                            if temp:
                                ans.append(temp)
                            s = []
                            break
                        else:
                            s.append(line[i])
                            i += 1
                    else:
                        s.append(line[i])
                        i += 1
                else:
                    if line[i] == '*':
                        if i + 1 < len(line) and line[i + 1] == '/':
                            multi = False
                            i += 1
                    i += 1
            else:
                if not multi:
                    temp = ''.join(s)
                    if temp:
                        print(temp)
                        ans.append(temp)
                    s = []
        temp = ''.join(s)
        if temp:
            print(temp)
            ans.append(temp)

        return ans
        

                            
