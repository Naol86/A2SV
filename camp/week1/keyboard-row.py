class Solution:
    def findWords(self, words: List[str]) -> List[str]:
        row_one = set(["q","w","e","r","t","y","u","i","o","p","Q","W","E","R","T","Y","U","I","O","P"])
        row_two = set(["a","s","d","f","g","h","j","k","l","A","S","D","F","G","H","J","K","L"])
        row_three = set(["z","x","c","v","b","n","m","Z","X","C","V","B","N","M"])
        dic = {1:row_one, 2:row_two , 3:row_three}
        ans = []
        for i in words:
            temp = -1
            if i[0] in row_one:
                temp = 1
            elif i[0] in row_two:
                temp = 2
            else:
                temp = 3
            row = dic[temp]
            for j in i:
                if j not in row:
                    break
            else:
                ans.append(i)
        return ans