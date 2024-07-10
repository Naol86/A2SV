# Problem: Remove Sub-Folders from the Filesystem - https://leetcode.com/problems/remove-sub-folders-from-the-filesystem/

class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end = False

class Solution:
    def __init__(self):
        self.root = TrieNode()
        self.ans = []

    def insert(self, path):
        path = path.split('/')
        cur = self.root
        for _file in path[1:]:
            if _file not in cur.children:
                cur.children[_file] = TrieNode()
            cur = cur.children[_file]
        cur.is_end = True
        # print(self.root.children[''].children)
    
    def find(self, cur, ans):
        for children in cur.children:
            ans.append(children)
            if not cur.children[children].is_end:
                self.find(cur.children[children], ans.copy())
                ans.pop()
                continue
            self.ans.append('/'.join(ans))
            ans.pop()

    def removeSubfolders(self, folder: List[str]) -> List[str]:
        for path in folder:
            self.insert(path)
        self.find(self.root, [''])
        # print(self.ans)
        return self.ans
        