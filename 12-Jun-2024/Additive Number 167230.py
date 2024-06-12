# Problem: Additive Number - https://leetcode.com/problems/additive-number/

class Solution:
    def isAdditiveNumber(self, num: str) -> bool:
        valid = []
        # num = [i for i in num]
        temp = []
        def back_tracking(i):
            if len(temp) > 1:
                x = temp[0] + temp[1]
                temp2 = temp.copy()
                temp2.append(x)
                st = str(x)
                join = [str(temp[0]), str(temp[1]), st]
                # i += len(st)
                
                while i < len(num) and st == num[i: i + len(st)]:
                    # print(st)
                    x = temp2[-1] + temp2[-2]
                    i += len(st)
                    st = str(x)
                    if i >= len(num):
                        break
                    temp2.append(x)
                    join.append(st)

                # join.pop()
                # print(temp2)
                # print(''.join(join))
                if ''.join(join) == num and len(join) > 2:
                    return True
                return False
            for j in range(i,len(num)):
                temp.append(int(num[i:j+1]))
                x = back_tracking(j + 1)
                temp.pop()
                if x:
                    return True
            return False
        x = back_tracking(0)
        # print(x)
        return x

                    
