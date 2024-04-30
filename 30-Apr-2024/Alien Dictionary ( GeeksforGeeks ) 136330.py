# Problem: Alien Dictionary ( GeeksforGeeks ) - https://www.geeksforgeeks.org/problems/alien-dictionary/1

#User function Template for python3
from collections import defaultdict, deque
class Solution:
    def findOrder(self,alien: dict, N, K):
        graph = defaultdict(list)
        inDegree = defaultdict(int)
        def path(x, y):
            for i in range(min(len(x), len(y))):
                if x[i] != y[i]:
                    if y[i] not in graph[x[i]]:
                        inDegree[y[i]] += 1
                        graph[x[i]].append(y[i])
                    inDegree[x[i]]
                    # inDegree[x[i]] -= 1
                    return True
            if len(x) > len(y):
                return False
            return True
        for i in range(N-1):
            path(alien[i], alien[i+1])
        ans = []
        sets = set()
        queue = deque()
        for key, val in inDegree.items():
            if val == 0:
                queue.append(key)
        # print(graph)
        # print(inDegree)
        # print(queue)
        while queue:
            x = queue.popleft()
            ans.append(x)
            sets.add(x)
            for node in graph[x]:
                inDegree[node] -= 1
                if inDegree[node] == 0:
                    queue.append(node)
        for i in range(K):
            if chr(ord('a') + i) not in sets:
                ans.append(chr(ord('a') + i))
                
        # print(queue)
        return ''.join(ans)
    # code here



#{ 
 # Driver Code Starts
#Initial Template for Python 3

class sort_by_order:
    def __init__(self,s):
        self.priority = {}
        for i in range(len(s)):
            self.priority[s[i]] = i
    
    def transform(self,word):
        new_word = ''
        for c in word:
            new_word += chr( ord('a') + self.priority[c] )
        return new_word
    
    def sort_this_list(self,lst):
        lst.sort(key = self.transform)

if __name__ == '__main__':
    t=int(input())
    for _ in range(t):
        line=input().strip().split()
        n=int(line[0])
        k=int(line[1])
        
        alien_dict = [x for x in input().strip().split()]
        duplicate_dict = alien_dict.copy()
        ob=Solution()
        order = ob.findOrder(alien_dict,n,k)
        s = ""
        for i in range(k):
            s += chr(97+i)
        l = list(order)
        l.sort()
        l = "".join(l)
        if s != l:
            print(0)
        else:
            x = sort_by_order(order)
            x.sort_this_list(duplicate_dict)
            
            if duplicate_dict == alien_dict:
                print(1)
            else:
                print(0)


# } Driver Code Ends